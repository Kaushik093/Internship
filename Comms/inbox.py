import imaplib
import email

host = 'imap.gmail.com'
username = 'roboticarm69@gmail.com'
password = 'Roboticarm@69'

mail = imaplib.IMAP4_SSL(host=host)
mail.login(username, password)
mail.select("inbox")

_, search_data = mail.search(None, 'UNSEEN')

for num in search_data[0].split():
    print(num)
    _, data = mail.fetch(num, '(RFC822)')
    _, b = data[0]
    msg_str = str(b)
    print('msg_str', msg_str)