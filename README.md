# Offline YouTube Video Summarizer

## 1. Project Overview

This project is an **end-to-end offline AI system** that accepts a YouTube video URL, downloads the audio, transcribes the speech into text, and generates a concise summary.

All AI models (speech-to-text and summarization) run **entirely offline** on the local machine without relying on any cloud-based APIs.

The application includes both:

* a **command-line interface (CLI)**, and
* a **Streamlit-based web interface** for easier interaction and demonstration.

---

## 2. Setup and Installation Instructions

### System Requirements

* Python 3.10+
* ffmpeg (required for audio processing)

Install ffmpeg:

```bash
sudo apt update
sudo apt install ffmpeg -y
```

---

### Python Environment Setup

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### Model Download (Offline Setup)

* Whisper (speech-to-text) and BART (summarization) models are **automatically downloaded on first run**
* Models are stored locally inside the `models/` directory
* After the initial download, the system runs fully offline

---

## 3. Design Choices and Justification

### Speech-to-Text Model

* **Model:** Whisper (via faster-whisper)
* **Reason for Choice:**

  * High transcription accuracy
  * Open-source and offline-capable
  * Optimized CPU inference using faster-whisper
* **Trade-off:**

  * Slightly slower on CPU compared to GPU, but acceptable for offline processing

---

### Summarization Model

* **Model:** facebook/bart-large-cnn
* **Reason for Choice:**

  * Strong abstractive summarization performance
  * Well-suited for long-form text
  * Stable and widely used in production systems
* **Trade-off:**

  * Larger model size increases inference time on CPU

---

### Architecture Decisions

* Modular pipeline design:

  * Downloader
  * Transcriber
  * Chunker
  * Summarizer
* **Hierarchical summarization** is used to safely handle long transcripts by:

  * Summarizing individual chunks
  * Generating a final summary from chunk summaries
* Backend logic is decoupled from the UI, allowing easy extension to other interfaces (CLI, web, API)

---

## 4. Usage

### Streamlit Web Interface (Recommended)

Run the application:

```bash
streamlit run app_streamlit.py
```

Steps:

1. Open the Streamlit URL in the browser
2. Enter a YouTube video link
3. View real-time progress logs
4. Receive the generated summary

---

### Command-Line Interface (Optional)

```bash
python main.py
```

Enter a YouTube URL when prompted.

---

## 5. Challenges Faced and Solutions

### Handling Long Videos

* **Problem:** Language models have context length limits
* **Solution:** Implemented chunking and hierarchical summarization

---

### Offline Constraints

* **Problem:** Models must run without cloud APIs
* **Solution:** Used open-source models and local caching of model weights

---

### YouTube Extraction Variability

* **Problem:** YouTube streaming formats change frequently
* **Solution:** Used yt-dlp, which robustly selects the best available audio format and logs warnings without breaking the pipeline

---

### User Feedback During Long Processing

* **Problem:** Long-running tasks appear unresponsive
* **Solution:** Added progress tracking, logs, and percentage updates in the Streamlit UI

---

## 6. Demonstration

A short screencast video is included demonstrating:

* Entering a YouTube URL
* Audio download
* Transcription
* Summarization
* Final output display

---

## 7. Robustness

* Invalid URLs are caught and reported
* Progress and error logs are displayed clearly
* Long videos are handled safely using chunking
* Failures in any stage are logged and surfaced to the user

---

## 8. Project Structure

```
app/                # Core pipeline logic
main.py             # CLI entry point
app_streamlit.py    # Streamlit UI
models/             # Local model storage (ignored in git)
data/               # Runtime data (ignored in git)
requirements.txt
README.md
```

---

