# import smtplib
# from email.message import EmailMessage
# from string import Template
from pathlib import Path
#
#
# def send_email(email_to, decision_type, name):
#     html = Template(Path('index.html').read_text())
#     email = EmailMessage()
#     email['from'] = 'College Decision Simulator Bot'
#     email['to'] = email_to
#     email['subject'] = decision_type
#
#     email.set_content(html.substitute({'name': name}), 'html')
#
#     with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#         smtp.ehlo()
#         smtp.starttls()
#         smtp.login('mukhammadkodirmakhmudjanov@gmail.com', 'QW34ty78opkl')
#         smtp.send_message(email)
#         print("All done!")

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, subject, smtp_username, smtp_password):
    # Read the contents of the HTML file
    with open('utils/misc/index.html', 'r') as f:
        html_body = f.read()

    # Create an email message object with HTML body
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(html_body, "html"))

    # Create a SMTP client object and send the message
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)

