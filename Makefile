.PHONY: install update

# Define variables for commands
PYTHON=python3
APP_EXECUTABLE=run.py
APP_NAME=run
HOST=0.0.0.0
PORT=8000
GUNICORN=gunicorn
WORKERS=1

# Use environment variable FLASK_ENV to determine dev or prod mode
FLASK_ENV ?= development  # Default to development if not set

# Installing dependencies
install:
	poetry install

# Validate all code quality & linting errors
format:
	isort .
	black --line-length 70 .
	flake8 --ignore=E501

# Run tests
test:
	poetry install --no-root

# Check coverage
coverage:
	pytest --cov

# Clean up .pyc files
clean:
	find . -name "*.pyc" -exec rm -f {} \;

# Start Flask app using Gunicorn, adjust for environment
run:
ifeq ($(FLASK_ENV), production)
	@echo "Running in production mode"
	$(GUNICORN) --bind $(HOST):$(PORT) $(APP_NAME):app --workers $(WORKERS)
else
	@echo "Running in development mode"
	$(PYTHON) $(APP_EXECUTABLE)
endif
