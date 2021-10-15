import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'roboticarm69@gmail.com'
password = 'Roboticarm@69'

def send_email(text = 'Email Body', subject = 'Tasks', to_emails = None, html = None):
    assert isinstance(to_emails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = '<Robotic Arm> roboticarm69@gmail.com'
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail('Robotic Arm roboticarm69@gmail.com', to_emails, msg=msg_str)

    server.quit()