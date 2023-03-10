import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from environs import Env
env = Env()
env.read_env()

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

