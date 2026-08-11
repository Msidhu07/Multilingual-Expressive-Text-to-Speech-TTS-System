import subprocess
import os
from gtts import gTTS

# ---------------- Models ----------------

EN_MODEL = "models/en_US-lessac-medium.onnx"
HI_MODEL = "models/hi_IN-pratham-medium.onnx"
TE_MODEL = "models/te_IN-maya-medium.onnx"

# ---------------- Output ----------------

OUTPUT = os.path.join("outputs", "speech.wav")

# ---------------- Piper ----------------

PIPER = r"C:\Users\Jeshw\Downloads\piper_windows_amd64\piper\piper.exe"


def generate_speech(text, language, emotion="Neutral"):

    os.makedirs("outputs", exist_ok=True)

    # ---------- Kannada (gTTS) ----------

    if language == "Kannada":

        print("Generating Kannada Speech...")

        tts = gTTS(
            text=text,
            lang="kn"
        )

        tts.save(OUTPUT)

        print("Speech saved at:", OUTPUT)

        return OUTPUT

    # ---------- Select Piper Model ----------

    if language == "English":
        model = EN_MODEL

    elif language == "Hindi":
        model = HI_MODEL

    elif language == "Telugu":
        model = TE_MODEL

    else:
        raise Exception(f"Unsupported language: {language}")

    # ---------- Piper Check ----------

    if not os.path.exists(PIPER):
        raise Exception("Piper executable not found.")

    # ---------- Generate Speech ----------

    command = [
        PIPER,
        "--model",
        model,
        "--output_file",
        OUTPUT,
    ]

    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )

    stdout, stderr = process.communicate(text)

    if stdout:
        print("STDOUT:", stdout)

    if stderr:
        print("STDERR:", stderr)

    if process.returncode != 0:
        raise Exception(f"Piper Error:\n{stderr}")

    if not os.path.exists(OUTPUT):
        raise Exception("Speech file was not created.")

    print("Speech generated successfully.")

    return OUTPUT