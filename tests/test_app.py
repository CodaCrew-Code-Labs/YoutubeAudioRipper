import os
from unittest.mock import patch

import pytest

from app import create_app


def cleanup_logs_directory():
    """Helper function to remove the logs directory if it exists."""
    if os.path.exists("logs"):
        for root, dirs, files in os.walk("logs", topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir("logs")  # Finally, remove the logs directory itself


def setup_logging():
    """Set up logging by ensuring the logs directory exists."""
    if not os.path.exists("logs"):
        os.makedirs("logs")


@pytest.fixture
def client():
    """Create a test client using the app's factory function."""
    # Set the environment variable for testing purposes
    with patch.dict(os.environ, {"FLASK_ENV": ""}):
        app = create_app()
        app.config["TESTING"] = True  # Set testing mode
        with app.test_client() as client:
            yield client


def test_create_app_default_to_development():
    """Test that when no FLASK_ENV is set, it defaults to DevelopmentConfig."""
    app = create_app()
    assert (
        app.config["DEBUG"] is True
    )  # Assuming DEBUG=True in DevelopmentConfig


def test_create_app_production_environment():
    """Test that when FLASK_ENV is set to production,
    it uses ProductionConfig."""
    with patch.dict(os.environ, {"FLASK_ENV": "production"}):
        app = create_app()
        assert (
            app.config["DEBUG"] is False
        )  # Assuming DEBUG=False in ProductionConfig


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Fixture to clean up before and after tests."""
    cleanup_logs_directory()  # Clean up before each test
    yield
    cleanup_logs_directory()  # Clean up after each test


def test_setup_logging_creates_logs_directory():
    """Test that the logs directory is created if it doesn't exist."""
    with patch("os.makedirs") as mock_makedirs, patch(
        "os.path.exists"
    ) as mock_exists:
        # Configure the mock to return False,
        # simulating that the logs directory doesn't exist
        mock_exists.return_value = False

        # Call the setup_logging function
        setup_logging()

        # Assert that os.makedirs was called
        # to create the logs directory
        mock_makedirs.assert_called_once_with("logs")


def test_setup_logging_directory_exists():
    """Test that no directory is created if it already exists."""
    # Mock os.path.exists to return True
    with patch("os.path.exists", return_value=True), patch(
        "os.makedirs"
    ) as mock_makedirs:

        # Call the setup_logging function
        setup_logging()

        # Assert that os.makedirs was not called
        mock_makedirs.assert_not_called()
