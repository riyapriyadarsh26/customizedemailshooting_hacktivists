import mysql.connector
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Title
st.title("Customized Email Sender")

# Collect user input
#recipient_email = st.text_input("Recipient's Email:")
subject = st.text_input("Subject:")
message = st.text_area("Message:")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="theaqueen1",
  database="bingustest"
)

cursor = mydb.cursor()

recipients = []
cursor.execute("SELECT email FROM bingus")
recipient_email = cursor.fetchall()
for i in range(len(recipient_email)):
    recipients.append(recipient_email[i][0])

# Send email when the user clicks the button
if st.button("Send Email"):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = "shuvayusarkar38@gmail.com"
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject

        body = message
        msg.attach(MIMEText(body, 'plain'))

        # Connect to your SMTP server and send the email
        smtp_server = "smtp.gmail.com" 
        smtp_port = 587
        username = "shuvayusarkar38@gmail.com"
        password = "walkwegirdzwlcpa"

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, recipients, msg.as_string())        
        server.quit()

        st.success("Email sent successfully!")

    except Exception as e:
        st.error(f"Error: {str(e)}")

        