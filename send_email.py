#calling python libraries 

import os

import smtplib

from email.message import EmailMessage

from email.utils import formataddr

from pathlib import PurePath

from dotenv import load_dotenv 

PORT = 587
EMAIL_SERVER = "smtp-mail.gmail.com"

#Load the environment variables
current_dir = Path(__file__).resolve().parent if"__file__" in locals() else Path.cwd()

envars = current_dir / ".env"
load_dotenv(envars)

#Read environment variables
sender_email = os.getenv("EMAIL")
Password_email = os.getenv("PASSWORD")






#actual function to send email

def send_email(subject, receiver_email, name, company)