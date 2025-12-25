# app/pipeline.py

from app.downloader import download_audio
from app.transcriber import transcribe
from app.chunker import chunk_text
from app.summarizer import summarize_chunks
from app.logger import setup_logger

logger = setup_logger()

def run_pipeline(url: str, progress_callback=None) -> str:
    def update(msg, pct=None):
        logger.info(msg)
        if progress_callback:
            progress_callback(msg, pct)

    try:
        update("Starting pipeline", 5)

        update("Downloading audio", 15)
        audio = download_audio(url)

        update("Transcribing audio (this may take time)", 40)
        text = transcribe(audio)

        update("Chunking transcript", 55)
        chunks = chunk_text(text)

        update(f"Generated {len(chunks)} chunks", 65)

        update("Summarizing content", 85)
        summary = summarize_chunks(chunks)

        update("Pipeline completed successfully", 100)
        return summary

    except Exception as e:
        update(f"Pipeline failed: {e}", 100)
        raise
