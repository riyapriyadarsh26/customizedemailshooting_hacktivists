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
sender_email = os.getenv("shuvayusarkar38@gmail.com")
Password_email = os.getenv("walkwegirdzwlcpa")






#actual function to send email 

def send_email(subject, receiver_email, name, company_name):
    #create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("NIT GOA Training and Placement Cell", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    