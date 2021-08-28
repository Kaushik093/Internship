import imaplib
import email

host = 'imap.gmail.com'
username = 'roboticarm69@gmail.com'
password = 'Roboticarm@69'

def read():
    new = []
    mail = imaplib.IMAP4_SSL(host=host)
    mail.login(username, password)
    mail.select("inbox")

    _, search_data = mail.search(None, 'UNSEEN')

    for num in search_data[0].split():
        data = []
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        msg_str = str(b)
        email_message = email.message_from_bytes(b)

        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                body_str = body.decode("UTF-8")
                new.append(body_str)
    
    return new