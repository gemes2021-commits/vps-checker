import requests
import smtplib
from email.mime.text import MIMEText
import os

URL = "https://panel.hostoff.net/services/virtual-servers/order"

def send_email(subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = os.environ["EMAIL_SENDER"]
    msg["To"] = os.environ["EMAIL_RECEIVER"]

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(
            os.environ["EMAIL_SENDER"],
            os.environ["EMAIL_PASSWORD"]
        )
        server.send_message(msg)

def check():
    response = requests.get(URL, timeout=10)
    text = response.text.lower()

    if "нет в наличии" not in text:
        send_email(
            "🔥 VPS доступны!",
            f"Сервера появились: {URL}"
        )
        print("AVAILABLE")
    else:
        print("NOT AVAILABLE")

check()
