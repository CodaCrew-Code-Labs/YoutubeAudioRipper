<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/github_banner.png" alt="Logo" width="300" height="150">
  </a>

  <h3 align="center">YouTube Audio Ripper </h3>

  <p align="center">
    A simple tool that extracts audio from YouTube videos and shorts
    <br />
    <b>A PodGaze Library Project</b>
    <br />
    <a href="https://github.com/CodaCrew-Code-Labs/YoutubeAudioRipper"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/CodaCrew-Code-Labs/YoutubeAudioRipper/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/CodaCrew-Code-Labs/YoutubeAudioRipper/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>


## Table of Contents

- [Project Description](#project-description)
- [Built With](#built-with)
- [Installation Instructions](#installation-instructions)
- [Features](#features)
- [Changelog](#changelog)
- [API Documentation](#api-documentation)
- [License](#license)


## Project Description

This Flask app allows users to download YouTube videos by providing a URL, convert the video to an MP3 file, and then store the resulting file in an Amazon S3 bucket. This app can be used for personal, academic, or project purposes to easily convert and manage audio files extracted from YouTube videos.


## Built With

This section list frameworks/libraries used to bootstrap the project as well as the current status of the package.


#### Repo Info

[![license][license]][license-url]
[![issues-shield][issues-shield]][issues-url]
[![lastcommit-shield][lastcommit-shield]][lastcommit-url] 
[![github-release][github-release]][github-release-url]
[![Pr-request][Pr-request]][Pr-request-url]
[![Repo-size][Repo-size]][Repo-size-url]
[![Forks][Forks]][Forks-url]


#### Library Info

[![Python][Python]][Python-url] 
[![Docker][Docker]][Docker-url] 
[![Swagger][Swagger]][Swagger-url] 
[![Flask][Flask]][Flask-url] 
[![Flake8][Flake8]][Flake8-url]
[![Black][Black]][Black-url]  
[![Poetry][Poetry]][Poetry-url]  


#### Last Build Details

[![Github-build][Github-build]][Github-build-url]
[![Codecov][Codecov]][Codecov-url]
[![Codefactor][Codefactor]][Codefactor-url]
[![Codacy][Codacy]][Codacy-url]
[![Scrutinizer][Scrutinizer]][Scrutinizer-url]


#### Supported Platforms

[![Linux][Linux]][Linux-url]
[![Windows][Windows]][Windows-url]
[![MacOS][MacOS]][MacOS-url]
[![Cloud][Cloud]][Cloud-url]


#### Other Apps

* [Snyk](https://app.snyk.io/org/codacrew-code-labs)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Installation Instructions

### Prerequisites

- **Python 3.12.7+** should be installed on your system.
- **AWS S3** credentials configured for storage.
- **FFmpeg** installed for media conversion (for converting videos to MP3).

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/your-flask-app.git
   cd your-flask-app
   ```

2. **Install Prerequisites**:
    
    ```bash
    Install Make
    pip install poetry
    ```

3. **Create a Virtual Environment**:

   ```bash
   pip install poetry
   poetry shell
   ```

4. **Install Dependencies**:

   ```bash
   poetry install
   ```

5. **Set Up Environment Variables**:

   Create a `.env` file in the root directory with the following:

   ```bash
    FLASK_ENV=development
    AWS_ACCESS_KEY_ID=your_aws_access_key
    AWS_SECRET_ACCESS_KEY=your_aws_secret_key
    AWS_SESSION_TOKEN=your_aws_session_token #If accessed via a role
    DB_USER=your_sql_db_user
    DB_PASSWORD=your_db_password
    DB_HOSTNAME=your_db_endpoint
    DB_PORT=your_db_port
    DEFAULT_DB=default_db
   ```

6. **FFmpeg Installation**:

   - Ensure that FFmpeg is installed on your machine for the app to handle media conversion. You can install it using:

     ```bash
     sudo apt install ffmpeg  # For Linux
     brew install ffmpeg      # For macOS
     ```

   - **Windows**: Download and set up FFmpeg from [here](https://ffmpeg.org/download.html).

7. **Run the Application**:

   ```bash
   make run
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

- Download YouTube videos by providing a URL.
- Convert downloaded video files to MP3 format.
- Store converted MP3 files in an AWS S3 bucket.
- Secure and scalable storage using AWS S3.
- API endpoint to trigger the video conversion and upload.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Changelog

### v1.0.0
- Initial release.
- Basic functionality of downloading YouTube video, converting to MP3, and storing in S3.
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## API Documentation
Yet to add the link

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

This project is licensed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python]: https://img.shields.io/badge/python-3.12.7-blue?style=for-the-badge&logo=python&logoColor=yellow
[Python-url]: https://www.python.org/
[Swagger]: https://img.shields.io/badge/swagger-Ready-green?style=for-the-badge&logo=swagger&logoColor=white
[Swagger-url]: https://swagger.io/
[Flask]: https://img.shields.io/badge/flask-3.0.3-black?style=for-the-badge&logo=flask
[Flask-url]: https://flask.palletsprojects.com/
[Black]: https://img.shields.io/badge/code_style-black-black?style=for-the-badge
[Black-url]: https://pypi.org/project/black/
[Flake8]: https://img.shields.io/badge/linter-flake8-yellow?style=for-the-badge
[Flake8-url]: https://flake8.pycqa.org/
[issues-shield]: https://img.shields.io/github/issues/CodaCrew-Code-Labs/YoutubeAudioRipper.svg?style=for-the-badge
[issues-url]: https://github.com/CodaCrew-Code-Labs/YoutubeAudioRipper
[lastcommit-shield]: https://img.shields.io/github/last-commit/CodaCrew-Code-Labs/YoutubeAudioRipper?style=for-the-badge
[lastcommit-url]: https://github.com/CodaCrew-Code-Labs/YoutubeAudioRipper
[github-release]: https://img.shields.io/github/v/release/CodaCrew-Code-Labs/YoutubeAudioRipper?style=for-the-badge
[github-release-url]: https://github.com/CodaCrew-Code-Labs/YoutubeAudioRipper
[license]:https://img.shields.io/badge/license-mit-green?style=for-the-badge
[license-url]:https://github.com/CodaCrew-Code-Labs/YoutubeAudioRipper/LICENSE
[docker]: https://img.shields.io/badge/docker-enabled-black?style=for-the-badge&logo=docker
[docker-url]: https://www.docker.com/
[Poetry]: https://img.shields.io/badge/dependency_management-poetry-blue?style=for-the-badge&logo=poetry&logoColor=blue
[Poetry-url]: https://python-poetry.org/
[Github-build]: https://img.shields.io/github/actions/workflow/status/CodaCrew-Code-Labs/YoutubeAudioRipper/flask-build.yml?style=for-the-badge
[Github-build-url]: https://github.com/CodaCrew-Code-Labs/YoutubeAudioRipper/actions/workflows/flask-build.yml
[Codecov]: https://img.shields.io/codecov/c/github/CodaCrew-Code-Labs/YoutubeAudioRipper/dev?style=for-the-badge
[Codecov-url]: https://github.com/CodaCrew-Code-Labs/YoutubeAudioRipper
[Pr-request]: https://img.shields.io/github/issues-pr/CodaCrew-Code-Labs/YoutubeAudioRipper?style=for-the-badge
[Pr-request-url]: https://github.com/CodaCrew-Code-Labs/YoutubeAudioRipper
[Repo-size]: https://img.shields.io/github/repo-size/CodaCrew-Code-Labs/YoutubeAudioRipper?style=for-the-badge
[Repo-size-url]: https://github.com/CodaCrew-Code-Labs/YoutubeAudioRipper
[Forks]: https://img.shields.io/github/forks/CodaCrew-Code-Labs/YoutubeAudioRipper?style=for-the-badge
[Forks-url]: https://github.com/CodaCrew-Code-Labs/YoutubeAudioRipper
[Linux]: https://img.shields.io/badge/platform-linux-brightgreen?style=for-the-badge
[Linux-url]: https://www.linux.org/
[Windows]: https://img.shields.io/badge/platform-windows-blue?style=for-the-badge
[Windows-url]:  https://www.microsoft.com/en-us/windows
[MacOS]: https://img.shields.io/badge/platform-macOS-lightgrey?style=for-the-badge
[MacOS-url]:  https://www.apple.com/macos/  
[Cloud]: https://img.shields.io/badge/platform-Cloud-orange?style=for-the-badge
[Cloud-url]: https://aws.amazon.com/cloud/
[Codefactor]: https://img.shields.io/codefactor/grade/github/CodaCrew-Code-Labs/YoutubeAudioRipper?style=for-the-badge&logo=codefactor&label=CodeFactor
[Codefactor-url]: https://www.codefactor.io/repository/github/codacrew-code-labs/youtubeaudioripper
[Codacy]: https://img.shields.io/codacy/grade/c75aad4375bc416696c80b4553f653b6/dev?style=for-the-badge&logo=codacy&label=Codacy
[Codacy-url]: https://app.codacy.com/gh/CodaCrew-Code-Labs/YoutubeAudioRipper/dashboard
[Scrutinizer]: https://img.shields.io/scrutinizer/quality/g/CodaCrew-Code-Labs/YoutubeAudioRipper?style=for-the-badge&label=Scrutinizer%20Code%20Quality
[Scrutinizer-url]: https://scrutinizer-ci.com/g/CodaCrew-Code-Labs/YoutubeAudioRipper/
