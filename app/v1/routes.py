import os
import random
import string
from datetime import datetime

import boto3
from flask import Blueprint, current_app, jsonify, request
from moviepy.editor import AudioFileClip
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix.exceptions import RegexMatchError, VideoUnavailable
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename

from app.models import USERVALIDATIONRELATION, YTVIDEOLIST, db

# Define a Blueprint for the routes
main_routes = Blueprint("v1", __name__)

# Initialize S3 client
s3 = boto3.client("s3")


def generate_random_id(length=10):
    # Define the characters to choose from: alphanumeric
    characters = string.ascii_letters + string.digits
    # Generate a random ID
    random_id = "".join(random.choices(characters, k=length))
    return random_id


def update_db(new_row):
    try:
        db.session.add(new_row)
        db.session.commit()  # Commit the transaction
    except IntegrityError as e:
        db.session.rollback()  # Rollback in case of an error
        print(f"IntegrityError occurred: {e}")
    except Exception as e:
        db.session.rollback()  # Rollback for any other exception
        print(f"An error occurred: {e}")
    finally:
        db.session.remove()


@main_routes.route("/", methods=["GET"])
def hello():
    """
    A greeting endpoint for Version 1.
    ---
    responses:
        200:
            description: A greeting message
    """

    # Logger
    current_app.logger.info("Data received: %s", "Testing Tested")

    return "This is version 1 of the API"


@main_routes.route("/validate", methods=["GET"])
def validate_url():
    """
    YouTube URL Validation endpoint.
    ---
    parameters:
        - name: yturl
          in: query
          type: string
          required: true
          description: URL of the YT Video or Short Form Content
    responses:
        200:
            description: URL Validation Success Message
            schema:
                type: object
                properties:
                    requested_url:
                        type: string
                        example: https://www.youtube.com/shorts/eU13jvC8_sI
                    status:
                        type: string
                        example: SUCCESS
        422:
            description: URL Validation Invalid Format Error Message
            schema:
                type: object
                properties:
                    status:
                        type: string
                        example: ERROR
                    error:
                        type: string
                        example: "Missing parameter 'yturl'"
        400:
            description: Parameter Missing In The Request Error
            schema:
                type: object
                properties:
                    requested_url:
                        type: string
                        example: https://www.youtube.com/shorts/eU13jvC8_sI
                    status:
                        type: string
                        example: ERROR
                    error:
                        type: string
                        example: "URL Format is not valid"
    """

    # Get the specific query parameter 'param1'
    yt_url = request.args.get("yturl")

    # Logger
    current_app.logger.info("Given Youtube URL", yt_url)

    if yt_url is None:
        return (
            jsonify(
                {
                    "status": "ERROR",
                    "error": "Missing parameter 'yturl'",
                }
            ),
            400,
        )

    try:
        YouTube(yt_url)
    except RegexMatchError:
        return (
            jsonify(
                {
                    "requested_url": yt_url,
                    "status": "ERROR",
                    "error": "URL Format is not valid",
                }
            ),
            422,
        )
    except VideoUnavailable:
        return (
            jsonify(
                {
                    "requested_url": yt_url,
                    "status": "ERROR",
                    "error": "is NOT a valid YouTube URL",
                }
            ),
            409,
        )

    return (
        jsonify({"requested_url": yt_url, "status": "SUCCESS"}),
        200,
    )


@main_routes.route("/convert", methods=["POST"])
def mp3_converter():
    """
    YouTube URL To MP3 Converter API.
    ---
    parameters:
        - name: yturl
          in: query
          type: string
          required: true
          description: URL of the YT Video or Short Form Content
        - name: user
          in: query
          type: string
          required: true
          description: User id of the requester
        - name: project
          in: query
          type: string
          required: true
          description: Project id for the requesting file
    responses:
        200:
            description: Audio Conversion Success Message
            schema:
                type: object
                properties:
                    requested_url:
                        type: string
                        example: https://www.youtube.com/shorts/eU13jvC8_sI
                    status:
                        type: string
                        example: SUCCESS
                    message:
                        type: string
                        example: File uploaded successfully
                    filename:
                        type: string
                        example: yt_files/audio_20241020_023956.mp3
        400:
            description: Parameter Missing In The Request Error
            schema:
                type: object
                properties:
                    status:
                        type: string
                        example: ERROR
                    error:
                        type: string
                        example: "URL Format is not valid"
        409:
            description: Video Already Uploaded Error
            schema:
                type: object
                properties:
                    status:
                        type: string
                        example: ERROR
                    error:
                        type: string
                        example: "Video Already Uploaded"
        500:
            description: Unhandled Exception Error
            schema:
                type: object
                properties:
                    status:
                        type: string
                        example: ERROR
                    error:
                        type: string
                        example: "Unknown Exception"
    """

    # Fetch values from environment variables
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    aws_session_token = os.environ.get(
        "AWS_SESSION_TOKEN"
    )  # Fetch the session token

    # Define your S3 bucket name
    s3_bucket = "podgaze"

    # Initialize the S3 client with the fetched values
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,  # Include the session token
        region_name="us-east-1",
    )

    # Get the specific query parameter 'param1'
    yt_url = request.args.get("yturl")
    username = request.args.get("user")
    userproject = request.args.get("project")

    if yt_url is None:
        return (
            jsonify(
                {
                    "status": "ERROR",
                    "error": "Missing parameter 'yturl'",
                }
            ),
            400,
        )
    elif username is None:
        return (
            jsonify(
                {
                    "status": "ERROR",
                    "error": "Missing parameter 'user'",
                }
            ),
            400,
        )
    elif userproject is None:
        return (
            jsonify(
                {
                    "status": "ERROR",
                    "error": "Missing parameter 'project'",
                }
            ),
            400,
        )

    try:
        yt = YouTube(yt_url, on_progress_callback=on_progress)

        # Setting Audio Properties
        # Random Video Audio File ID
        audio_file_id = generate_random_id()

        mp3_filename = "audio.mp3"

        # Making MP3 ready for the upload
        original_filename = secure_filename(mp3_filename)

        # Extract the file extension
        file_extension = os.path.splitext(original_filename)[
            1
        ]  # e.g., '.mp3'

        # Get current date
        current_date = datetime.now().strftime(
            "%Y%m%d"
        )  # Format: YYYYMMDD
        current_timestamp = datetime.now().strftime(
            "%H%M%S"
        )  # Format: HHMMSS

        # Create new filename
        audio_file_name = f"audio_{current_date}_{current_timestamp}{file_extension}"
        new_filename = f"yt_files/{audio_file_name}"

        # Check if the YouTube URL already exists in the database
        video_already_available = (
            db.session.query(YTVIDEOLIST)
            .filter_by(yt_id=yt.video_id)
            .first()
        )

        if video_already_available is not None:
            current_app.logger.info("Video already available in db")

            audio_file_id = video_already_available.video_id

            # Video exists, now check if it's associated with the user
            user_video_relation = (
                db.session.query(USERVALIDATIONRELATION)
                .filter_by(user_id=username, video_id=audio_file_id)
                .first()
            )

            if user_video_relation:
                return (
                    jsonify(
                        {
                            "status": "ERROR",
                            "error": "Video already Present",
                        }
                    ),
                    409,
                )

        elif video_already_available is None:
            current_app.logger.info("Video not in db")

            audio_stream = yt.streams.filter(only_audio=True).first()

            if audio_stream is None:
                return (
                    jsonify(
                        {
                            "status": "ERROR",
                            "error": "No audio present in the link",
                        }
                    ),
                    400,
                )

            current_app.logger.info(
                f"Downloading audio: {yt.title}..."
            )
            audio_file = audio_stream.download(
                filename="audio.mp4"
            )  # Download as mp4 first

            # Convert the downloaded audio to mp3
            audio_clip = AudioFileClip(audio_file)
            audio_clip.write_audiofile(mp3_filename)  # Convert to mp3
            audio_clip.close()

            # # Remove the temporary mp4 file
            os.remove(audio_file)

            # Upload the file to S3
            try:
                # Open the file in binary mode
                with open(mp3_filename, "rb") as f:
                    s3_client.upload_fileobj(
                        f, s3_bucket, new_filename
                    )

                # update newly updated video in db
                new_video = YTVIDEOLIST(
                    video_id=audio_file_id,
                    yt_id=yt.video_id,
                    s3_filename=audio_file_name,
                )

                update_db(new_video)

                # # Remove the temporary mp4 file
                os.remove(mp3_filename)

            except Exception as e:
                return (
                    jsonify(
                        {
                            "status": "ERROR",
                            "error": str(e),
                        }
                    ),
                    500,
                )

        # Random Relation ID
        relation_id = generate_random_id()

        # Should continue from updating the user db
        new_relation = USERVALIDATIONRELATION(
            relation_id=relation_id,
            user_id=username,
            video_id=audio_file_id,
            project_id=userproject,
            updated_date=datetime.utcnow(),  # Set the updated date to current time
        )

        update_db(new_relation)

        return (
            jsonify(
                {
                    "requested_url": yt_url,
                    "status": "SUCCESS",
                    "message": "File uploaded successfully",
                    "filename": new_filename,
                }
            ),
            200,
        )

    except Exception as e:
        return (
            jsonify(
                {
                    "status": "ERROR",
                    "error": str(e),
                }
            ),
            500,
        )
