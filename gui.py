import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Title
st.title("Customized Email Sender")

# Collect user input
recipient_email = st.text_input("Recipient's Email:")
subject = st.text_input("Subject:")
message = st.text_area("Message:")

# Send email when the user clicks the button
if st.button("Send Email"):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = "shuvayusarkar38@gmail.com"
        msg['To'] = recipient_email
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
        server.sendmail(username, recipient_email, msg.as_string())
        server.quit()

        st.success("Email sent successfully!")

    except Exception as e:
        st.error(f"Error: {str(e)}")

        