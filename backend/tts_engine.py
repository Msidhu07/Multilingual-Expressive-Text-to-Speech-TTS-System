import os
import subprocess
import torch

from transformers import VitsModel, AutoTokenizer
from scipy.io.wavfile import write


# ============================================================
# PATHS
# ============================================================

EN_MODEL = "models/en_US-lessac-medium.onnx"
TE_MODEL = "models/te_IN-maya-medium.onnx"
HI_MODEL = "models/hi_IN-pratham-medium.onnx"

# Offline Kannada MMS model
KN_MODEL = "models/kannada-mms"

OUTPUT = "outputs/speech.wav"

PIPER = r"C:\Users\Jeshw\Downloads\piper_windows_amd64\piper\piper.exe"


# ============================================================
# LOAD KANNADA MODEL ONCE
# ============================================================

print("Loading offline Kannada model...")

try:
    kannada_tokenizer = AutoTokenizer.from_pretrained(KN_MODEL)
    kannada_model = VitsModel.from_pretrained(KN_MODEL)

    print("Kannada offline model loaded successfully!")

except Exception as e:
    print("Kannada model loading failed:")
    print(e)

    kannada_tokenizer = None
    kannada_model = None


# ============================================================
# KANNADA SPEECH
# ============================================================

def generate_kannada_speech(text):

    if kannada_tokenizer is None or kannada_model is None:
        raise Exception("Kannada offline model is not loaded.")

    print("Using offline Kannada MMS model...")

    inputs = kannada_tokenizer(
        text,
        return_tensors="pt"
    )

    with torch.no_grad():
        output = kannada_model(**inputs).waveform

    os.makedirs("outputs", exist_ok=True)

    write(
        OUTPUT,
        kannada_model.config.sampling_rate,
        output.squeeze().cpu().numpy()
    )

    print("Kannada speech generated successfully.")
    print("Saved:", OUTPUT)

    return OUTPUT


# ============================================================
# MAIN SPEECH GENERATION
# ============================================================

def generate_speech(text, language, emotion="Neutral"):

    os.makedirs("outputs", exist_ok=True)

    # --------------------------------------------------------
    # Validate text
    # --------------------------------------------------------

    if not text or not text.strip():
        raise Exception("Text cannot be empty.")

    text = text.strip()

    # --------------------------------------------------------
    # KANNADA - FULLY OFFLINE
    # --------------------------------------------------------

    if language == "Kannada":

        return generate_kannada_speech(text)

    # --------------------------------------------------------
    # PIPER LANGUAGES
    # --------------------------------------------------------

    if language == "English":
        model = EN_MODEL

    elif language == "Telugu":
        model = TE_MODEL

    elif language == "Hindi":
        model = HI_MODEL

    else:
        raise Exception(
            f"Unsupported language: {language}"
        )

    # --------------------------------------------------------
    # Check Piper
    # --------------------------------------------------------

    if not os.path.exists(PIPER):
        raise Exception(
            f"Piper executable not found:\n{PIPER}"
        )

    # --------------------------------------------------------
    # Check model
    # --------------------------------------------------------

    if not os.path.exists(model):
        raise Exception(
            f"TTS model not found:\n{model}"
        )

    # --------------------------------------------------------
    # Piper command
    # --------------------------------------------------------

    command = [
        PIPER,
        "--model",
        model,
        "--output_file",
        OUTPUT,
    ]

    print(f"Using Piper model: {model}")
    print(f"Generating {language} speech...")

    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )

    stdout, stderr = process.communicate(text)

    print("Piper STDOUT:")
    print(stdout)

    print("Piper STDERR:")
    print(stderr)

    # --------------------------------------------------------
    # Check process
    # --------------------------------------------------------

    if process.returncode != 0:
        raise Exception(
            f"Piper speech generation failed:\n{stderr}"
        )

    # --------------------------------------------------------
    # Check output
    # --------------------------------------------------------

    if not os.path.exists(OUTPUT):
        raise Exception(
            "Speech file was not created."
        )

    if os.path.getsize(OUTPUT) == 0:
        raise Exception(
            "Generated speech file is empty."
        )

    print(f"{language} speech generated successfully.")
    print("Saved:", OUTPUT)

    return OUTPUT