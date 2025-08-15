---

# 📧 AI-Powered Gmail Assistant

An intelligent email automation tool built in Python that connects to your Gmail inbox, classifies unread messages, and uses **Groq’s LLaMA model** to suggest concise and polite replies.
You can **review, edit, and send** AI-suggested responses directly from your terminal using the **Gmail API**.

---

## 🚀 Features

* **Fetch Unread Emails** – Retrieves unread messages from your Gmail inbox.
* **AI-Powered Replies** – Generates polite, context-aware responses using Groq’s LLaMA model.
* **User Review & Editing** – Approve, modify, or reject AI-suggested replies before sending.
* **Direct Gmail Integration** – Send replies instantly using the Gmail API.
* **Threaded Replies** – Maintains proper conversation threading with `In-Reply-To` and `References` headers.

---

## 🛠 Tech Stack

* **Python** – Core scripting language.
* **Groq API** – AI model for reply generation.
* **Google Gmail API** – Email reading and sending.
* **OAuth 2.0** – Secure authentication with Google services.
* **dotenv** – For environment variable management.

---

## 📂 Project Structure

```
your-project/
│  main.py
│  credentials.json        # Google API credentials
│  token.pickle            # Generated after first login
│  .env                    # Stores GROQ_API_KEY
│  requirements.txt
└─ services/
   │  gmail.py              # Gmail API functions (read, send)
   └  ai.py                 # Groq AI integration
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ai-gmail-assistant.git
cd ai-gmail-assistant
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up Google Cloud Project**

   * Go to [Google Cloud Console](https://console.cloud.google.com/)
   * Create a new project.
   * Enable **Gmail API**.
   * Create OAuth 2.0 credentials and download `credentials.json` into the project root.

4. **Set Groq API Key**
   Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

5. **Run the assistant**

```bash
python main.py
```

---

## 🖼 How It Works

1. Authenticate with Gmail on first run.
2. The script fetches the latest unread emails.
3. Groq’s AI generates suggested replies.
4. You can choose to **send**, **edit**, or **skip** each reply.
5. If approved, the email is sent instantly via Gmail API.

---

## 🔒 Security Notes

* Your Gmail credentials are **never stored in plaintext**. OAuth tokens are stored locally in `token.pickle`.
* Always keep your `credentials.json` and `.env` file private and out of version control (`.gitignore`).

---

## 👤 Author

**Suyash Singh Gusain**

* 🌐 [GitHub]((https://github.com/suyash-codes))
* 💼 [LinkedIn](www.linkedin.com/in/suyashsinghgusain)

---
