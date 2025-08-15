import base64
from email.mime.text import MIMEText


def send_email(service, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    send_message = service.users().messages().send(userId="me", body={'raw': raw_message}).execute()
    print(f"✅ Email sent! Message ID: {send_message['id']}")
