import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from datetime import datetime

# Get the current date and time
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# from environs import Env
# env = Env()
# env.read_env()

from data import config

university_dictionary = {
    'acceptance': {
        'stanford': 'utils/misc/decision_letters/Stanford/stanford_acceptance.html',
        'harvard': 'utils/misc/decision_letters/Harvard/harvard_acceptance.html',
        'yale': 'utils/misc/decision_letters/Yale/yale_acceptance.html',
        'dartmouth': 'utils/misc/decision_letters/Dartmouth/dartmouth_acceptance.html',
        'duke': 'utils/misc/decision_letters/Duke/duke_acceptance.html',
        'nyuad': 'utils/misc/decision_letters/NYUAD/nyuad_acceptance.html',
        'princeton': 'utils/misc/decision_letters/Princeton/princeton_acceptance.html',
        'uchicago': 'utils/misc/decision_letters/Uchicago/uchicago_acceptance.html'
    },
    'rejection': {
        'harvard': 'utils/misc/decision_letters/Harvard/harvard_rejection.html',
        'yale': 'utils/misc/decision_letters/Yale/yale_rejection.html',
        'dartmouth': 'utils/misc/decision_letters/Dartmouth/dartmouth_rejection.html',
        'duke': 'utils/misc/decision_letters/Duke/duke_rejection.html',
        'nyuad': 'utils/misc/decision_letters/NYUAD/nyuad_rejection.html',
        'princeton': 'utils/misc/decision_letters/Princeton/princeton_rejection.html',
        'uchicago': 'utils/misc/decision_letters/Uchicago/uchicago_rejection.html',
        'stanford': 'utils/misc/decision_letters/Stanford/stanford_rejection.html'
    }
}


def send_email2(sender_name, receiver_email, first_name, decision, university):
    # Replace with your SMTP credentials and SES region
    smtp_username = config.SMTP_USERNAME
    smtp_password = config.SMTP_PASSWORD
    aws_region = config.AWS_REGION

    # Replace with the verified email address associated with your SES account
    sender_email = 'simulator@college-decision.com'

    with open(university_dictionary[decision][university], 'r') as f:
        html_body = f.read()

    # Add dynamic content to HTML body
    html_body = html_body.replace('Dear,', f'Dear {first_name},')
    html_body = html_body.replace('time_date', f'Dear {current_date},')

    # Set up the email message
    message = MIMEMultipart("alternative")
    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = receiver_email
    message["Subject"] = "View Update to your Application!"
    message.attach(MIMEText(html_body, "html"))

    # Connect to the Amazon SES SMTP server
    smtp_server = smtplib.SMTP('email-smtp.' + aws_region + '.amazonaws.com', 587)
    smtp_server.starttls()

    # Log in to the SMTP server
    smtp_server.login(smtp_username, smtp_password)

    # Send the email
    smtp_server.sendmail(sender_email, receiver_email, message.as_string())

    # Disconnect from the server
    smtp_server.quit()