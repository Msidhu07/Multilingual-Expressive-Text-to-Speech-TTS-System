import { useState } from "react";
import axios from "axios";

function TTSForm() {
  const [text, setText] = useState("");
  const [language, setLanguage] = useState("English");
  const [emotion, setEmotion] = useState("Neutral");
  const [voice, setVoice] = useState("Default");

  const [audioUrl, setAudioUrl] = useState("");
  const [selectedFile, setSelectedFile] = useState(null);

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const wordCount =
    text.trim() === "" ? 0 : text.trim().split(/\s+/).length;

  const copyText = () => {
    navigator.clipboard.writeText(text);
    setMessage("📋 Text copied successfully.");
    setError("");
  };

  const clearText = () => {
    setText("");
    setAudioUrl("");
    setSelectedFile(null);
    setMessage("");
    setError("");
  };

  const generateSpeech = async () => {
    if (!text.trim()) {
      setError("Please enter some text.");
      return;
    }

    setLoading(true);
    setAudioUrl("");
    setMessage("");
    setError("");

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/generate",
        {
          text,
          language,
          emotion,
          voice,
        },
        {
          responseType: "blob",
        }
      );

      const url = URL.createObjectURL(response.data);

      setAudioUrl(url);
      setMessage("✅ Speech generated successfully!");

    } catch (err) {
      console.error(err);
      setError("❌ Error generating speech.");
    } finally {
      setLoading(false);
    }
  };

  const uploadPDF = async () => {
    if (!selectedFile) {
      setError("Please choose a PDF file.");
      return;
    }

    const formData = new FormData();

    formData.append("file", selectedFile);
    formData.append("language", language);
    formData.append("emotion", emotion);

    setLoading(true);
    setMessage("");
    setError("");

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/generate-pdf",
        formData,
        {
          responseType: "blob",
        }
      );

      const url = URL.createObjectURL(response.data);

      setAudioUrl(url);
      setMessage("✅ PDF converted to speech!");

    } catch (err) {
      console.error(err);
      setError("❌ Failed to convert PDF.");
    } finally {
      setLoading(false);
    }
  };

  const uploadTXT = async () => {
    if (!selectedFile) {
      setError("Please choose a TXT file.");
      return;
    }

    const formData = new FormData();

    formData.append("file", selectedFile);
    formData.append("language", language);
    formData.append("emotion", emotion);

    setLoading(true);
    setMessage("");
    setError("");

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/generate-txt",
        formData,
        {
          responseType: "blob",
        }
      );

      const url = URL.createObjectURL(response.data);

      setAudioUrl(url);
      setMessage("✅ TXT converted to speech!");

    } catch (err) {
      console.error(err);
      setError("❌ Failed to convert TXT.");
    } finally {
      setLoading(false);
    }
  };

  return (
        <div className="container">

      <h1 className="title">
        🎤 Multilingual Expressive TTS
      </h1>

      <p className="subtitle">
        Convert text into natural sounding speech in multiple Indian languages
      </p>

      {/* ================= Input Card ================= */}

      <div className="card">

        <h2>📝 Input Text</h2>

        <textarea
          rows="6"
          value={text}
          maxLength={500}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter your text here..."
        />

        <div className="counter">
          <span>Words : {wordCount}</span>
          <span>{text.length}/500</span>
        </div>

        <br />

        <div className="button-row">

          <button
            className="copy"
            onClick={copyText}
          >
            📋 Copy
          </button>

          <button
            className="clear"
            onClick={clearText}
          >
            🗑 Clear
          </button>

        </div>

      </div>

      {/* ================= Settings Card ================= */}

      <div className="card">

        <h2>⚙️ Speech Settings</h2>

        <div className="grid">

          <div>

            <label><b>🌐 Language</b></label>

            <br /><br />

            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
            >
              <option>English</option>
              <option>Hindi</option>
              <option>Telugu</option>
              <option>Kannada</option>
            </select>

          </div>

          <div>

            <label><b>😊 Emotion</b></label>

            <br /><br />

            <select
              value={emotion}
              onChange={(e) => setEmotion(e.target.value)}
            >
              <option>Neutral 😐</option>
              <option>Happy 😊</option>
              <option>Sad 😢</option>
              <option>Angry 😠</option>
              <option>Excited 🤩</option>
            </select>

          </div>

          <div>

            <label><b>🎙 Voice</b></label>

            <br /><br />

            <select
              value={voice}
              onChange={(e) => setVoice(e.target.value)}
            >
              <option>Default</option>
              <option>Female</option>
              <option>Male</option>
            </select>

          </div>

        </div>

      </div>

      {/* ================= Upload Card ================= */}

      <div className="card">

        <h2>📂 Upload PDF / TXT</h2>

        <input
          type="file"
          accept=".pdf,.txt"
          onChange={(e) => setSelectedFile(e.target.files[0])}
        />

        {selectedFile && (

          <p
            style={{
              color: "green",
              marginTop: "15px",
            }}
          >
            📄 {selectedFile.name}
          </p>

        )}

        <br />

        <div className="button-row">

          <button
            className="pdf"
            onClick={uploadPDF}
          >
            📄 PDF to Speech
          </button>

          <button
            className="txt"
            onClick={uploadTXT}
          >
            📄 TXT to Speech
          </button>

        </div>

      </div>

      {/* ================= Output Card ================= */}

      <div className="card">

        <h2>🎧 Generated Audio</h2>

        <button
          className="primary"
          onClick={generateSpeech}
          disabled={loading}
        >
          {loading
            ? "⏳ Generating..."
            : "🎙 Generate Speech"}
        </button>

        <br />
        <br />

        {message && (
          <div className="success">
            {message}
          </div>
        )}

        {error && (
          <div className="error">
            {error}
          </div>
        )}
                {audioUrl && (
          <>
            <hr style={{ marginTop: "25px", marginBottom: "25px" }} />

            <h3
              style={{
                textAlign: "center",
                marginBottom: "20px",
              }}
            >
              🎧 Generated Audio
            </h3>

            <audio
              controls
              src={audioUrl}
            />

            <div
              style={{
                textAlign: "center",
                marginTop: "20px",
              }}
            >
              <a
                href={audioUrl}
                download="speech.wav"
                className="download"
              >
                ⬇ Download Speech
              </a>
            </div>

            <div
              className="card"
              style={{
                marginTop: "25px",
              }}
            >
              <h3>📋 Speech Information</h3>

              <p>
                <strong>🌐 Language :</strong> {language}
              </p>

              <p>
                <strong>😊 Emotion :</strong> {emotion}
              </p>

              <p>
                <strong>🎙 Voice :</strong> {voice}
              </p>

              <p>
                <strong>🎵 Output :</strong> WAV Audio
              </p>

              <p>
                <strong>📝 Words :</strong> {wordCount}
              </p>

              <p>
                <strong>🔠 Characters :</strong> {text.length}
              </p>
            </div>
          </>
        )}

      </div>

      <p className="footer">
  © 2026 Multilingual Expressive TTS <br />
  Developed using React • FastAPI • Piper • MMS VITS
</p>

    </div>
  );
}

export default TTSForm;