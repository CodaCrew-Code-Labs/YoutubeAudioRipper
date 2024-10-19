import logging
import os
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
from flask import Flask

from app.database import db  # Import db from the new database module
from app.models import create_tables
from app.v1.routes import main_routes as v1
from flask_cors import CORS

from .config import DevelopmentConfig, ProductionConfig

load_dotenv()


def create_app(config_class=None):
    app = Flask(__name__)
    CORS(app)

    # Determine the environment and load the appropriate config
    if config_class is None:
        if os.environ.get("FLASK_ENV") == "production":
            config_class = ProductionConfig
        else:
            config_class = DevelopmentConfig

    app.config.from_object(config_class)

    # Load database URL
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    db_hostname = os.environ.get("DB_HOSTNAME")
    db_port = os.environ.get("DB_PORT")
    default_db = os.environ.get("DEFAULT_DB")

    # Create the database URL
    db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_hostname}:{db_port}/{default_db}"

    # Create the database URL
    db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_hostname}:{db_port}/{default_db}"

    # Set the SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url

    # Initialize the SQLAlchemy instance
    db.init_app(app)

    # Set up logging
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Configure file handler
    file_handler = RotatingFileHandler(
        "logs/app.log", maxBytes=10240, backupCount=10
    )
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s: %(message)s"
    )
    file_handler.setFormatter(formatter)

    # Add file handler to the app's logger
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)

    # Register Blueprints
    app.register_blueprint(v1, url_prefix="/v1")

    # Print the configuration values
    app.logger.info(f"ENV: {app.config['ENV']}")

    # Create tables if they do not exist
    create_tables(app)

    return app
