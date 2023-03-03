import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from environs import Env
env = Env()
env.read_env()

university_dictionary = {
    'acceptance': {
        'harvard': 'utils/misc/decision_letters/Harvard/harvard_acceptance.html'
    },
    'rejection': {
        'harvard': 'utils/misc/decision_letters/Harvard/harvard_rejection.html'
    }
}

def send_email(sender_name, sender_email, receiver_email, first_name, decision, university):
    # Read the contents of the HTML file
    with open(university_dictionary[decision][university], 'r') as f:
        html_body = f.read()

    # Add dynamic content to HTML body
    html_body = html_body.replace('Dear,', f'Dear {first_name},')

    # Create an email message object with HTML body
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    message = MIMEMultipart("alternative")
    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = receiver_email
    message["Subject"] = "View Update to your Application!"
    message.attach(MIMEText(html_body, "html"))

    # Create a SMTP client object and send the message
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(env.str("SMTP_USERNAME"), env.str("SMTP_PASSWORD"))
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)

