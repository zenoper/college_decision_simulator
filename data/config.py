from environs import Env
env = Env()
env.read_env()
#
# BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
# IP = env.str("ip")
# #
# DB_USER = env.str("DB_USER")
# DB_PASS = env.str("DB_PASS")
# DB_NAME = env.str("DB_NAME")
# DB_HOST = env.str("DB_HOST")

#
# SMTP_USERNAME = env.str("SMTP_USERNAME")
# SMTP_PASSWORD = env.str("SMTP_PASSWORD")
# AWS_REGION = env.str("AWS_REGION")



import os
#
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
# ADMINS = list(os.environ.get("ADMINS"))
# IP = str(os.environ.get("ip"))

DB_USER = str(os.environ.get("DB_USER"))
DB_PASS = str(os.environ.get("DB_PASS"))
DB_NAME = str(os.environ.get("DB_NAME"))
DB_HOST = str(os.environ.get("DB_HOST"))

SMTP_USERNAME = str(os.environ.get("SMTP_USERNAME"))
SMTP_PASSWORD = str(os.environ.get("SMTP_PASSWORD"))
AWS_REGION = str(os.environ.get("AWS_REGION"))