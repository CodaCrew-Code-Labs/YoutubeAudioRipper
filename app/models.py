from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String

from app.database import db  # Import the db instance


# Database model for YouTube video records
class YTVIDEOLIST(db.Model):
    __tablename__ = "yt_video_list"

    video_id = Column(String(10), primary_key=True)
    yt_id = Column(
        String(20), nullable=False, unique=True
    )  # Unique YouTube URL
    s3_filename = Column(
        String(255), nullable=False
    )  # S3 path of the uploaded file


# Database model for user video relations
class USERVALIDATIONRELATION(db.Model):
    __tablename__ = "user_video_relation"

    relation_id = Column(String(10), primary_key=True)
    user_id = Column(String(100), nullable=False)  # User's name
    video_id = Column(
        String(10),
        ForeignKey("yt_video_list.video_id"),
        nullable=False,
    )  # Use the correct column name
    project_id = Column(String(100), nullable=False)  # Project name
    updated_date = Column(DateTime, default=datetime.utcnow)


def create_tables(app):
    with app.app_context():  # Ensure the app context is available
        db.create_all()  # This will create all the tables defined in your models
    print("Tables created successfully")
