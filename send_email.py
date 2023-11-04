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
m





#actual function to send email 

def send_email(subject, receiver_email, name, company_name):
    #create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("NIT GOA Training and Placement Cell", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        I take this opportunity to introduce myself, This is Riya Priyadarshi, Sr. Placement Officer of National institute of technology Goa,</p>
          <p>Ponda,Goa. As a part of our continuous strives to bring the top companies to the college premises, We would like to request you to</p>
           <p> consider the possibilities of conducting your recruitment drive for B.Tech ( CS/IT, EC, EE, EIC, Mechanical, Electrical ),</p>
             <P>2023 Batch. We want to join hands with your esteemed organization and help our students to achieve a better career in your</p>
               <P>company. We will provide you quality entrant from required branches
    )