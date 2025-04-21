import smtplib
import logging
from email.mime.text import MIMEText


def send_email(to, subject, html_content, smtp_variable, files=None, cc=None, bcc=None):
    """
    Send an HTML email using SMTP configuration.

    Parameters:
        to (list[str]): List of recipient email addresses.
        subject (str): Subject of the email.
        html_content (str): The HTML content of the email body.
        smtp_variable (dict): Dictionary containing SMTP configuration keys:
            - smtp_host (str): SMTP server host.
            - smtp_port (int or str): SMTP server port.
            - smtp_user (str): SMTP username.
            - smtp_password (str): SMTP password.
            - smtp_mail_from (str): Email address to send from.
            - smtp_starttls (bool or str): Whether to use STARTTLS.
            - smtp_ssl (bool or str): Whether to use SSL.
        files (list[str], optional): List of file paths to attach (currently unused).
        cc (list[str], optional): List of CC email addresses (currently unused).
        bcc (list[str], optional): List of BCC email addresses (currently unused).

    Raises:
        Exception: If email sending fails, the exception is logged and re-raised.

    Notes:
        - Logs a success message for each recipient.
        - Automatically handles STARTTLS and SSL based on config.
    """
    logging.info(to)
    smtp_host = smtp_variable.get("smtp_host")
    smtp_port = int(smtp_variable.get("smtp_port"))
    smtp_user = smtp_variable.get("smtp_user")
    smtp_password = smtp_variable.get("smtp_password")
    smtp_mail_from = smtp_variable.get("smtp_mail_from")
    smtp_starttls = smtp_variable.get("smtp_starttls", True)
    smtp_ssl = smtp_variable.get("smtp_ssl", False)
    

    if isinstance(smtp_starttls, str):
        smtp_starttls = smtp_starttls.lower() == "true"
    if isinstance(smtp_ssl, str):
        smtp_ssl = smtp_ssl.lower() == "true"

    msg = MIMEText(html_content, 'html')
    msg["Subject"] = subject
    msg["CC"] = ','.join(to)
    try:

        if smtp_ssl:
            server = smtplib.SMTP_SSL(smtp_host, smtp_port)
        else:
            server = smtplib.SMTP(smtp_host, smtp_port)
            if smtp_starttls:
                server.starttls()

        if smtp_user and smtp_password:
            server.login(smtp_user, smtp_password)

        for client in to:
            server.sendmail(smtp_mail_from, client, msg.as_string())

            logging.info("Custom email sent successfully to %s", client)

        server.quit()
    except Exception as e:
        logging.error("Custom send_email failed: %s", e)
        raise






test_template = """<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #f6f6f6;
      margin: 0;
      padding: 20px;
    }}

    .container {{
      max-width: 800px;
      margin: 0 auto;
      background-color: #ffffff;
      border-radius: 8px;
      padding: 20px;
      border: 1px solid #ddd;
    }}

    h2 {{
      color: #333333;
      border-bottom: 2px solid #ddd;
      padding-bottom: 5px;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
      margin-bottom: 20px;
    }}

    th, td {{
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
      font-size: 14px;
    }}

    th {{
      background-color: #f2f2f2;
      font-weight: bold;
    }}

    .highlight {{
      font-weight: bold;
      color: #007BFF;
    }}

    .negative {{
      color: #dc3545;
    }}

    .positive {{
      color: #28a745;
    }}

    .normal {{
     color: black;
   }}
  </style>
</head>
<body>
  <div class="container">
    <h2>Báo cáo Tình hình Sức khỏe Công ty - Ngày {reported_date}</h2>
    <p><em>Các metrics được so sánh mức tăng giảm dựa trên giá trị trung bình của 7 ngày trước đó.</em></p>

    <h3>I. Chỉ số Kinh Doanh</h3>
    <table>
      <tr>
        <th>Mục tiêu</th>
        <th>Total</th>
        <th>{reported_date}</th>
        <th>% Biến động</th>
      </tr>
      <tr>
        <td>Cài đặt</td><td>{total_install}</td><td>{new_install}</td><td class="{percent_install_status}">{percent_install}</td>
      </tr>
      <tr>
        <td>Dân thể mới</td><td>{total_etag}</td><td>{new_etag}</td><td class="{percent_etag_status}">{percent_etag}</td>
      </tr>
      <tr>
        <td>Khách Hàng VETC</td><td>{total_vetc_customer}</td><td>{new_total_vetc_customer}</td><td class="{percent_total_vetc_customer_status}">{percent_total_vetc_customer}</td>
      </tr>
      <tr>
        <td>Cá Nhân</td><td>{total_vetc_customer_individual}</td><td>{new_vetc_customer_individual}</td><td class="{percent_vetc_individual_status}">{percent_vetc_individual}</td>
      </tr>
      <tr>
        <td>Doanh nghiệp</td><td>{total_vetc_customer_corporate}</td><td>{new_vetc_customer_corporate}</td><td class="{percent_vetc_corporate_status}">{percent_vetc_corporate}</td>
      </tr>
            <tr>
        <td>Chính Phủ</td><td>{total_vetc_customer_governance}</td><td>{new_vetc_customer_governance}</td><td class="{percent_vetc_governance_status}">{percent_vetc_governance}</td>
      </tr>
    </table>

    <h3>II. Chỉ số User</h3>
    <table>
      <tr>
        <th>Chỉ số</th>
        <th>Total</th>
        <th>{reported_date}</th>
        <th>% Biến động</th>
      </tr>
      <tr>
        <td>MAU</td><td></td><td>{MAU_new}</td><td></td>
      </tr>
      <tr>
        <td>WAU</td><td></td><td>{WAU_new}</td><td></td>
      </tr>
      <tr>
        <td>DAU</td><td></td><td>{DAU_new}</td><td></td>
      </tr>
      <tr>
        <td>DAU/MAU</td><td></td><td>{DAU_MAU}</td><td></td>
      </tr>
      <tr>
        <td>% E-Wallet / User App</td><td></td><td color='black'>{percent_E_wallet_users_new}</td><td></td>
      </tr>
      <tr>
        <td>E-Wallet</td><td>{total_ewallet_user}</td><td>{new_ewallet_user}</td><td class="{percent_ewallet_status}">{percent_ewallet}</td>
      </tr>
            <tr>
        <td>E-Wallet xác thực</td><td>{total_ewallet_user_verified}</td><td>{new_ewallet_user_verified}</td><td class="{percent_ewallet_verified_status}">{percent_ewallet_verified}</td>
      </tr>
            <tr>
        <td>E-Wallet liên kết ngân hàng</td><td>{total_ewallet_user_link_banking_account}</td><td>{new_ewallet_user_link_banking_account}</td><td class="{percent_ewallet_bank_status}">{percent_ewallet_bank}</td>
      </tr>
    </table>

    <h3>III. Chỉ số Marketing</h3>
    <table>
      <tr>
        <th>Mục tiêu</th>
        <th>Total</th>
        <th>{reported_date}</th>
        <th>% Biến động</th>
      </tr>
        <tr>
        <td><strong>ETC sang E-Wallet</strong></td><td></td><td></td><td></td>
      </tr>
      <tr>
        <td>ETC sang E-Wallet</td><td>{total_convert_from_etc_to_ewallet}</td><td>{new_user_upgrade_ewallet}</td><td class="{percent_convert_etc_status}">{percent_convert_etc}</td>
      </tr>
      <tr>
        <td>Ví điện tử đã xác thực</td><td>{total_convert_from_etc_to_ewallet_verified}</td><td>{new_user_ewallet_verify}</td><td class="{percent_convert_verified_status}">{percent_convert_verified}</td>
      </tr>
      <tr>
        <td><strong>Voucher sử dụng</strong></td><td>{total_redeem_voucher}</td><td>{daily_use_voucher}</td><td class="{percent_redeem_voucher_status}">{percent_redeem_voucher}</td>
      </tr>
    </table>

  </div>
</body>
</html>
"""

def auto_generate_status(context):
    for key in list(context.keys()):
        if "percent" in key:
            value_str = str(context[key]).strip()
            if value_str.startswith("-"):
                context[f"{key}_status"] = "negative"
            elif value_str.startswith("+"):
                context[f"{key}_status"] = "positive"
            else:
                context[f"{key}_status"] = "normal"

context ={}
reporting_template = test_template.format(**context)
