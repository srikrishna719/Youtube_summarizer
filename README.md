# YouTube Video Summarizer (Offline)

This project is an **end-to-end offline AI system** that takes a YouTube video link, converts the audio to text, and generates a concise summary — without using any cloud-based APIs.

The entire pipeline runs **locally** on CPU.

---

## What the System Does

1. Accepts a **YouTube URL**
2. Downloads the **audio** from the video
3. Converts speech to text using an **offline Whisper model**
4. Splits long transcripts into smaller chunks
5. Generates a summary using an **offline language model**
6. Displays progress and results via a **Streamlit web interface**

---

## Architecture

```
YouTube URL
   ↓
Audio Download (yt-dlp)
   ↓
Speech-to-Text (Whisper – offline)
   ↓
Chunking
   ↓
Hierarchical Summarization (LLM – offline)
   ↓
Final Summary
```

---

## Models Used (Offline)

* **Speech-to-Text:** Whisper (via faster-whisper)
* **Summarization:** facebook/bart-large-cnn

Models are downloaded once and stored locally.
After the first run, the system works completely offline.

---

## Tech Stack

* Python
* yt-dlp
* Whisper (faster-whisper)
* Hugging Face Transformers
* Streamlit
* ffmpeg

---

## How to Run

### System Requirement

```bash
sudo apt install ffmpeg -y
```

### Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run (Recommended)

```bash
streamlit run app_streamlit.py
```

Enter a YouTube URL in the browser to generate the summary.

---

## Key Features

* Fully offline AI pipeline
* Handles long videos using chunking + hierarchical summarization
* Live progress tracking and logs in UI
* Modular and clean architecture
* CPU-friendly (no GPU required)

---

## Limitations

* CPU inference can be slow for long videos
* YouTube extraction may show warnings due to platform changes
* First run takes time to download models

---

## Summary

This project demonstrates:

* Practical use of offline speech and language models
* End-to-end AI system design
* Robust handling of long-form content
* Clean separation between backend logic and UI
