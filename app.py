from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from PyPDF2 import PdfReader

from tts_engine import generate_speech

app = FastAPI(title="Multilingual Expressive TTS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- Request Model ----------------

class TTSRequest(BaseModel):
    text: str
    language: str
    emotion: str


# ---------------- Home ----------------

@app.get("/")
def home():
    return {
        "message": "Multilingual Expressive TTS API Running"
    }


# ---------------- Health ----------------

@app.get("/health")
def health():
    return {
        "status": "OK"
    }


# ---------------- Text to Speech ----------------

@app.post("/generate")
def generate(request: TTSRequest):

    audio_file = generate_speech(
        text=request.text,
        language=request.language,
        emotion=request.emotion
    )

    return FileResponse(
        path=audio_file,
        media_type="audio/wav",
        filename="speech.wav"
    )


# ---------------- PDF to Speech ----------------

@app.post("/generate-pdf")
async def generate_pdf(
    file: UploadFile = File(...),
    language: str = Form(...),
    emotion: str = Form(...)
):

    reader = PdfReader(file.file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    audio_file = generate_speech(
        text=text,
        language=language,
        emotion=emotion
    )

    return FileResponse(
        path=audio_file,
        media_type="audio/wav",
        filename="pdf_speech.wav"
    )


# ---------------- TXT to Speech ----------------

@app.post("/generate-txt")
async def generate_txt(
    file: UploadFile = File(...),
    language: str = Form(...),
    emotion: str = Form(...)
):

    text = file.file.read().decode("utf-8")

    audio_file = generate_speech(
        text=text,
        language=language,
        emotion=emotion
    )

    return FileResponse(
        path=audio_file,
        media_type="audio/wav",
        filename="text_speech.wav"
    )