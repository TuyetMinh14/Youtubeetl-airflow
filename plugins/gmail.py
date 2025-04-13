import smtplib
import logging
from email.mime.text import MIMEText

def send_email(to, subject, html_content, smtp_variable, files=None, cc=None, bcc=None):
    # Retrieve SMTP settings from the provided dictionary (or you could use Variable.get in Airflow)
    smtp_host       = smtp_variable.get("smtp_host")
    smtp_port       = int(smtp_variable.get("smtp_port"))
    smtp_user       = smtp_variable.get("smtp_user")
    smtp_password   = smtp_variable.get("smtp_password")
    smtp_mail_from  = smtp_variable.get("smtp_mail_from")
    smtp_starttls   = smtp_variable.get("smtp_starttls", False)    # Expecting a boolean or a string 'True'/'False'
    smtp_ssl        = smtp_variable.get("smtp_ssl", False)         # New key to indicate if SSL should be used

    # Normalize boolean values if they are provided as strings
    if isinstance(smtp_starttls, str):
        smtp_starttls = smtp_starttls.lower() == "true"
    if isinstance(smtp_ssl, str):
        smtp_ssl = smtp_ssl.lower() == "true"

    # Create MIME email message
    msg = MIMEText(html_content, 'html')
    msg["Subject"] = subject
    # msg["From"] = smtp_mail_from
    # msg["To"] = ["tonkhanhan1709@gmail.com"]

    try:
        # Use SMTP_SSL if smtp_ssl is True; otherwise use SMTP

        if smtp_ssl:
            server = smtplib.SMTP_SSL(smtp_host, smtp_port)
        else:
            server = smtplib.SMTP(smtp_host, smtp_port)
            # If not using SSL, check if we want to upgrade the connection using STARTTLS
            if smtp_starttls:
                server.starttls()

        # Log in if credentials are provided
        if smtp_user and smtp_password:
            server.login(smtp_user, smtp_password)

        # Send the email
        for client in to:
            server.sendmail(smtp_mail_from, client, msg.as_string())
            
            logging.info("Custom email sent successfully to %s", client)

        server.quit()
    except Exception as e:
        logging.error("Custom send_email failed: %s", e)
        raise

# Example SMTP settings dictionary configured for SSL (port 465 for Gmail):
smtp_variable = {
    "smtp_host": "smtp.gmail.com",
    "smtp_port": 465,
    "smtp_user": "thuanh14403@gmail.com",
    "smtp_password": "nfzk fofw hqjj extn",  # Remember to fill in your actual password or app-specific password here
    "smtp_mail_from": "thuanh14403@gmail.com",
    "smtp_ssl": True,         # Use SSL connection
    "smtp_starttls": False    # Not needed when using SMTP_SSL
}
import airflow.utils.email as airflow_email
airflow_email.send_email = send_email
