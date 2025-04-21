from airflow.models import Variable
import json


DAG_ID = Variable.get("DAG_ID", default_var='None')
YOUTUBE_API_KEY = Variable.get("YOUTUBE_API_KEY", default_var='None')

CLIENT_LIST = Variable.get("CLIENT_LIST", default_var=[], deserialize_json=True)



SMTP_HOST = Variable.get("SMTP_HOST", default_var='None')
SMTP_PORT = Variable.get("SMTP_PORT", default_var=465)
SMTP_USER = Variable.get("SMTP_USER",default_var='None')
SMTP_PASSWORD = Variable.get("SMTP_PASSWORD", default_var='None')
SMTP_MAIL_FROM = Variable.get("SMTP_MAIL_FROM", default_var='None')

SMTP_VARIABLE = {
    "smtp_host": SMTP_HOST,
    "smtp_port": SMTP_PORT,
    "smtp_user": SMTP_USER,
    "smtp_password": SMTP_PASSWORD,
    "smtp_mail_from": SMTP_MAIL_FROM,
    "smtp_ssl": True,
    "smtp_starttls": False
}

