from faster_whisper import WhisperModel
import os

WHISPER_MODEL_DIR = "models/whisper"
TRANSCRIPT_DIR = "data/transcripts"

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8",
    download_root=WHISPER_MODEL_DIR
)

def transcribe(audio_path: str) -> str:
    os.makedirs(TRANSCRIPT_DIR, exist_ok=True)

    segments, _ = model.transcribe(audio_path)
    text = " ".join(segment.text for segment in segments)

    out_file = os.path.basename(audio_path).replace(".wav", ".txt")
    out_path = f"{TRANSCRIPT_DIR}/{out_file}"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)

    return text
