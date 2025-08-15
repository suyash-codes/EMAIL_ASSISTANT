from gmail_service import gmail_authenticate, get_unread_emails
from groq_client import classify_email, draft_response
from utils import send_email

if __name__ == "__main__":
    service = gmail_authenticate()
    emails = get_unread_emails(service)

    if not emails:
        print("✅ No unread emails found.")
    else:
        for e in emails:
            print(f"\n📧 Subject: {e['subject']}")
            print(f"Snippet: {e['snippet']}")
            
            category = classify_email(e['subject'], e['snippet'])
            print(f"📌 Category: {category}")
            
            if category != "Spam":
                response_text = draft_response(e['subject'], e['snippet'])
                print(f"📝 Draft Response:\n{response_text}")
                # Uncomment to actually send the email:
                send_email(service, "suyash.alter@gmail.com", "Re: " + e['subject'], response_text)
