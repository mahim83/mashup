# Mashup Generator

## Project Overview

The Mashup Generator is a Python-based application that automatically creates a music mashup by downloading multiple songs of a specified singer from YouTube, converting them into audio format (MP3), trimming the first Y seconds from each track, and merging all trimmed audio clips into one final mashup file.

The project consists of two parts:

1. Program 1 – Command Line Interface (CLI)
2. Program 2 – Web Application (Flask-based)

---

## Program 1 – Command Line Application

File: `102303958.py`

This program runs locally using the terminal and generates a mashup file.

### Usage

```bash
python 102303958.py "<SingerName>" <NumberOfVideos> <AudioDuration> <OutputFileName>
```

### Example

```bash
python 102303958.py "Arijit Singh" 15 30 output.mp3
```

### Input Conditions

- NumberOfVideos must be greater than 10
- AudioDuration must be greater than 20 seconds

### Working Steps

1. Downloads N YouTube videos of the specified singer
2. Converts each video into MP3 format
3. Trims the first Y seconds from each audio file
4. Merges all trimmed audio clips
5. Produces the final mashup MP3 file

---

## Program 2 – Web Application

The web application provides a user-friendly interface built using Flask.

Live Web Application Link:

https://mashup-generator-4fe2.onrender.com

### Features

- User inputs:
  - Singer Name
  - Number of Videos
  - Duration (seconds)
  - Email ID
- Mashup is generated automatically
- Final output is compressed into a ZIP file
- ZIP file is sent to the user via Gmail SMTP

### Deployment Details

The web application is deployed using Render (Free Tier).

Build Command:
```
pip install -r requirements.txt
```

Start Command:
```
python app.py
```

Required Environment Variables:
- SENDER_EMAIL
- APP_PASSWORD

These variables are securely configured in the Render dashboard.

### Web Service Limitations

Since the application is hosted on Render Free Tier, the following issues may occur:

- FFmpeg may not be available in the cloud environment
- Limited RAM (approximately 512MB) may cause heavy video processing to fail
- Long-running mashup generation may result in request timeout
- YouTube downloads may fail due to cloud IP restrictions
- File storage is temporary and may reset after server restart

The CLI version works fully on a local machine where FFmpeg is properly installed.

---

## Technologies Used

- Python
- Flask
- yt-dlp
- MoviePy
- Pydub
- FFmpeg
- Gmail SMTP
- Git and GitHub
- Render (Cloud Hosting)

---

## Project Structure

```
mashup/
│
├── 102303958.py
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   └── form.html
└── README.md
```

---

## Local Requirements

- Python 3.x
- FFmpeg installed and added to system PATH
- Required libraries installed using:

```
pip install -r requirements.txt
```

---

## Author

Mahim Katiyar  
Thapar institute of engeneering and technology 
