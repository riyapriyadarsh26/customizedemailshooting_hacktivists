import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




def send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create a multipart message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Add body to the email
    msg.attach(MIMEText(message, "plain"))

    try:
        # Create a secure SSL/TLS connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()

        # Login to the SMTP server
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Close the SMTP connection
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email. Error:", str(e))

sender_email = "shuvayusarkar38@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "shuvayusarkar38@gmail.com"
smtp_password = "walkwegirdzwlcpa"
receiver_email="ssaravinth04@gmail.com"
subject="Invitation to participate in the campus recruitment "
body="I take this opportunity to introduce myself, This is Riya Priyadarshi, Sr. Placement Officer of National institute of technology Ponda,Goa. As a part of our continuous strives to bring the top companies to the college premises, We would like to request you to consider the possibilities of conducting your recruitment drive for B.Tech ( CS/IT, EC, EE, EIC, Mechanical, Electrical ),2023 Batch. We want to join hands with your esteemed organization and help our students to achieve a better career in your company. We will provide you quality entrant from required branches."
send_email(sender_email,receiver_email,subject,body,smtp_server,smtp_port,smtp_username,smtp_password)
