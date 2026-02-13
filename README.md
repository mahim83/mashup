# 🎵 Mashup Generator

## 📌 Project Overview

The Mashup Generator is a Python-based application that automatically creates a music mashup by:

- Downloading multiple songs of a specified singer from YouTube  
- Converting videos into audio format (MP3)  
- Trimming the first Y seconds from each audio file  
- Merging all trimmed audio clips into one final mashup  

This project includes:

- ✅ Program 1 – Command Line Interface (CLI)
- ✅ Program 2 – Web Application (Flask-based)

---

## 🖥 Program 1 – Command Line Application

**File:** `102303958.py`

This version runs locally using the terminal and generates a mashup file.

### ▶ Usage

```bash
python 102303958.py "<SingerName>" <NumberOfVideos> <AudioDuration> <OutputFileName>
```

### ▶ Example

```bash
python 102303958.py "Arijit Singh" 15 30 output.mp3
```

### ✅ Input Conditions

- `NumberOfVideos` must be greater than **10**
- `AudioDuration` must be greater than **20 seconds**

### 🔄 Processing Steps

1. Downloads N YouTube videos of the specified singer  
2. Converts each video into MP3 format  
3. Trims the first Y seconds from each audio file  
4. Merges all trimmed audio clips  
5. Produces a final mashup MP3 file  

---

## 🌐 Program 2 – Web Application

The Web Application provides a user-friendly interface built using **Flask**.

### 🔗 Live Web Application

https://mashup-generator-4fe2.onrender.com

### 🚀 Features

- User inputs:
  - Singer Name  
  - Number of Videos  
  - Duration (seconds)  
  - Email ID  

- Mashup is generated automatically  
- Final output is compressed into a ZIP file  
- ZIP file is sent to the user via Gmail  

---

## 🛠 Technologies Used

- Python  
- Flask  
- yt-dlp (YouTube downloading)  
- MoviePy (Video to audio conversion)  
- Pydub (Audio trimming and merging)  
- FFmpeg (Audio backend processing)  
- Gmail SMTP (Email sending)  
- Git & GitHub  
- Render (Cloud Deployment)  

---

## 📂 Project Structure

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

## 🚀 Deployment Details

The Web Application is deployed using **Render (Free Tier)**.

### Build Command

```
pip install -r requirements.txt
```

### Start Command

```
python app.py
```

### Required Environment Variables

- `SENDER_EMAIL`
- `APP_PASSWORD`

These variables are securely configured in the Render dashboard.

---

## 📧 Email Functionality

The application:

- Uses Gmail SMTP over SSL  
- Authenticates using a Gmail App Password  
- Sends the mashup as a ZIP attachment to the user  

---

## ⚠️ Known Limitations (Render Free Tier)

Because the web application is hosted on Render Free Tier:

- FFmpeg may not always be available in the cloud environment  
- Limited RAM (~512MB) may cause heavy video processing to fail  
- Long-running tasks may result in timeout errors  
- YouTube downloads may fail due to server restrictions  
- File storage is temporary and may reset after restart  

The CLI version works fully on a local machine with FFmpeg properly installed.

---

## 🧠 Local Requirements

- Python 3.x  
- FFmpeg installed and added to system PATH  
- Required libraries installed using:

```
pip install -r requirements.txt
```

---

## 👨‍💻 Author

Mahim Katiyar  
GitHub: https://github.com/mahim83
