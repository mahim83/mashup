from flask import Flask, render_template, request
import subprocess
import zipfile
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)


# ---------------- RUN CLI SCRIPT ----------------
def run_mashup(singer, videos, duration):
    cmd = [
        "py", "-3.12",
        "102303958.py",
        singer,
        str(videos),
        str(duration),
        "output.mp3"
    ]
    subprocess.run(cmd)


# ---------------- SEND EMAIL ----------------
def send_email(receiver_email):
    sender_email = "mahimkatiyar83@gmail.com"
    app_password = "ejnszveecgzdaggm"

    msg = EmailMessage()
    msg["Subject"] = "Your Mashup File"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Please find your mashup attached.")

    with open("mashup.zip", "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="zip",
            filename="mashup.zip"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)


# ---------------- ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        singer = request.form["singer"]
        videos = int(request.form["videos"])
        duration = int(request.form["duration"])
        email = request.form["email"]

        if videos <= 10 or duration <= 20:
            return "Videos must be >10 and duration >20"

        run_mashup(singer, videos, duration)

        # Create zip file
        with zipfile.ZipFile("mashup.zip", "w") as zipf:
            zipf.write("output.mp3")

        send_email(email)

        return "Mashup created and sent successfully!"

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
