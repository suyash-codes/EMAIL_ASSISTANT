import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def classify_email(subject, snippet):
    prompt = f"""
    Classify this email into one of these categories:
    - Urgent
    - Spam
    - Follow-up

    Subject: {subject}
    Body Snippet: {snippet}

    Only return the category name.
    """
    resp = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
    )
    content = resp.choices[0].message.content
    return content.strip() if content is not None else ""

def draft_response(subject, snippet):
    prompt = f"""
    Draft a short, polite, and relevant reply to this email:
    Subject: {subject}
    Body: {snippet}
    """
    resp = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
    )
    content = resp.choices[0].message.content
    return content.strip() if content is not None else ""
