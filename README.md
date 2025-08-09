# CodeAlpha_Task
A user-friendly language translation tool using Python, HTML, CSS, and JavaScript. Supports real-time translation via API with a clean, responsive UI. Ideal for quick, accurate text translation across multiple languages.
# 🌐 Flask Translation API

A simple RESTful API built with Flask that translates text between languages using the `googletrans` library. This service can be used in web applications, chatbot systems, or other services requiring multilingual support.

---

## 📌 Features

- Translate text between 100+ languages.
- Supports custom source and target languages.
- CORS enabled for easy integration with frontend applications.
- Lightweight and easy to deploy.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed (version 3.7+ recommended). Then, install the required Python packages:

```bash
pip install Flask flask-cors googletrans==4.0.0-rc1
```

---

## 🧑‍💻 Running the Application

To start the Flask server locally:

```bash
python translation-tool.py
```

The API will be accessible at:

```
http://localhost:8888/translate
```

---

## 📨 API Endpoint

### **POST** `/translate`

**Request Body (JSON):**

```json
{
  "text": "Hello world",
  "source": "en",       // Optional: source language code (e.g., "en")
  "target": "es"        // Required: target language code (e.g., "es")
}
```

**Response (JSON):**

```json
{
  "translated_text": "Hola mundo"
}
```

**Error Response (Missing fields):**

```json
{
  "error": "Missing required fields"
}
```

---

## 🔧 Example Usage

Using `curl`:

```bash
curl -X POST http://localhost:8888/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Good morning", "source": "en", "target": "fr"}'
```

**Response:**

```json
{
  "translated_text": "Bonjour"
}
```

---

## 📁 File Structure

```
.
├── translation-tool.py    # Main Flask application
└── README.md              # Project documentation
```

---

## ⚠️ Notes

- This app uses the `googletrans` library, which relies on unofficial Google Translate APIs. For production environments, consider using official APIs like Google Cloud Translation or Microsoft Azure Translator.
- The `source` language is optional; if omitted, the translator will attempt to auto-detect it.

---

## 📬 Contact

If you have any questions or need further improvements, feel free to reach out.
