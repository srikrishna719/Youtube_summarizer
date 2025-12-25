import yt_dlp
import os

AUDIO_DIR = "data/audio"

def download_audio(youtube_url: str) -> str:
    os.makedirs(AUDIO_DIR, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{AUDIO_DIR}/%(id)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "192",
        }],
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        video_id = info["id"]

    return f"{AUDIO_DIR}/{video_id}.wav"
