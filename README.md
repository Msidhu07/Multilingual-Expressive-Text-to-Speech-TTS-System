# 🎤 Multilingual Expressive Text-to-Speech (TTS) System

## 📌 Project Overview

The Multilingual Expressive Text-to-Speech (TTS) System is a web application that converts text into natural-sounding speech in multiple Indian languages. It is built using React for the frontend and FastAPI for the backend.

The system supports English, Hindi, Telugu, and Kannada. English, Hindi, and Telugu use Piper TTS for offline speech synthesis, while Kannada uses gTTS because a suitable offline open-source Kannada model was not available during development.

---

## ✨ Features

- 🎤 Text to Speech
- 🌐 English
- 🇮🇳 Hindi
- తెలుగు Telugu
- ಕನ್ನಡ Kannada
- 📄 PDF to Speech
- 📄 TXT File to Speech
- 😊 Emotion Selection
- 🎙 Voice Selection (UI)
- 📋 Copy Text
- 🗑 Clear Text
- 🔢 Character Counter
- 📝 Word Counter
- ⏳ Loading Indicator
- 🎧 Audio Player
- ⬇ Download Generated Audio
- 📱 Responsive UI

---

## 🛠 Technologies Used

### Frontend

- React.js
- Axios
- CSS

### Backend

- FastAPI
- Python

### TTS Models

- Piper TTS
- gTTS

### Other Libraries

- PyPDF2
- python-multipart

---

## 📂 Project Structure

```
Multilingual-TTS/

│
├── backend/
│   ├── app.py
│   ├── tts_engine.py
│   ├── models/
│   └── outputs/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── App.jsx
│   └── App.css
│
├── requirements.txt
├── README.md
└── report.pdf
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

## 🎯 Supported Languages

| Language | Engine |
|----------|--------|
| English | Piper |
| Hindi | Piper |
| Telugu | Piper |
| Kannada | gTTS |

---

## 📄 Supported File Formats

- TXT
- PDF

---

## 📷 Screenshots

Add screenshots here:

- Home Page
- Generate Speech
- PDF Upload
- TXT Upload
- Audio Player

---

## 📈 Future Improvements

- More Indian Languages
- Offline Kannada Model
- Emotion-based Speech Synthesis
- Speed Control
- Pitch Control

---

## 👨‍💻 Developed By

**M Sidhardha**

Computer Science Engineering

2026

---

## 📜 License

This project is developed for educational purposes.
