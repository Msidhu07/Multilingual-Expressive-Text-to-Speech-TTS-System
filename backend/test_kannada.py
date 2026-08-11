import torch
from transformers import VitsModel, AutoTokenizer
from scipy.io.wavfile import write

MODEL_PATH = "models/kannada-mms"

print("Loading Kannada model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = VitsModel.from_pretrained(MODEL_PATH)

text = "ನಮಸ್ಕಾರ. ನಮ್ಮ ಬಹುಭಾಷಾ ಪಠ್ಯದಿಂದ ಧ್ವನಿ ವ್ಯವಸ್ಥೆಗೆ ಸ್ವಾಗತ."

inputs = tokenizer(text, return_tensors="pt")

print("Generating Kannada speech...")

with torch.no_grad():
    output = model(**inputs).waveform

write(
    "outputs/kannada_test.wav",
    model.config.sampling_rate,
    output.squeeze().numpy()
)

print("Kannada speech generated successfully!")
print("Saved: outputs/kannada_test.wav")