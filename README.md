# Multilingual Expressive Text-to-Speech (TTS) System

A multilingual Text-to-Speech web application that converts text into speech for English, Hindi, Telugu, and Kannada.

The system provides a simple React-based web interface and a FastAPI backend. The core speech generation uses locally installed open-source TTS models and can run without an active internet connection after the required models and dependencies are installed.

---

## Features

- Text-to-Speech generation
- Support for four languages:
  - English
  - Hindi
  - Telugu
  - Kannada
- Local/offline speech generation
- Open-source TTS models
- Play generated audio in the browser
- Download generated speech as `.wav`
- Emotion selection in the UI
- Voice selection in the UI
- Character counter
- Word counter
- Copy text button
- Clear text button
- PDF to Speech
- TXT to Speech
- Loading indicator while generating speech
- Error and success messages
- Clean and responsive web interface

---

## Technology Stack

### Frontend

- React
- Vite
- Axios
- HTML/CSS

### Backend

- Python
- FastAPI
- Uvicorn

### TTS Engines

- Piper for English, Hindi, and Telugu
- MMS VITS for Kannada

All core speech generation is performed locally using installed models.

---

## Project Structure

```text
multilingual-expressive-tts/
│
├── backend/
│   ├── app.py
│   ├── tts_engine.py
│   ├── requirements.txt
│   ├── test_kannada.py
│   │
│   ├── models/
│   │   ├── en_US-lessac-medium.onnx
│   │   ├── te_IN-maya-medium.onnx
│   │   ├── hi_IN-pratham-medium.onnx
│   │   └── kannada-mms/
│   │
│   └── outputs/
│
├── frontend/
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   ├── index.html
│   │
│   └── src/
│       ├── App.jsx
│       ├── App.css
│       ├── index.css
│       ├── main.jsx
│       │
│       └── components/
│           └── TTSForm.jsx
│
├── report/
│   └── Project Report.pdf
│
├── screenshots/
│
└── README.md
