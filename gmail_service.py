import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.modify', 
          'https://www.googleapis.com/auth/gmail.send']


def gmail_authenticate():
    creds = None
    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as f:
            creds = pickle.load(f)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pkl', 'wb') as f:
            pickle.dump(creds, f)
    return build('gmail', 'v1', credentials=creds)

def get_unread_emails(service, max_results=5):
    resp = service.users().messages().list(
        userId='me', q='is:unread', maxResults=max_results
    ).execute()

    emails = []
    for m in resp.get('messages', []):
        msg = service.users().messages().get(userId='me', id=m['id']).execute()
        subject = next(h['value'] for h in msg['payload']['headers'] if h['name'] == 'Subject')
        snippet = msg.get('snippet')
        emails.append({'id': m['id'], 'subject': subject, 'snippet': snippet})
    return emails
