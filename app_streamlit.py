# app_streamlit.py

import streamlit as st
from app.pipeline import run_pipeline

st.set_page_config(
    page_title="Offline YouTube Summarizer",
    layout="centered"
)

st.title("📺 Offline YouTube Video Summarizer")
st.write("Enter a YouTube URL to generate an offline summary.")

youtube_url = st.text_input("YouTube URL")

# UI placeholders
progress_bar = st.progress(0)
status_text = st.empty()
log_box = st.empty()

logs = []

def progress_callback(message, percent):
    if percent is not None:
        progress_bar.progress(percent)
    logs.append(message)
    log_box.text("\n".join(logs[-8:]))  # show last 8 logs
    status_text.info(message)

if st.button("Generate Summary"):
    if not youtube_url.strip():
        st.warning("Please enter a valid YouTube URL.")
    else:
        logs.clear()
        progress_bar.progress(0)

        try:
            summary = run_pipeline(
                youtube_url,
                progress_callback=progress_callback
            )

            st.success("✅ Summary generated successfully!")
            st.subheader("📝 Summary")
            st.write(summary)

        except Exception as e:
            st.error(f"❌ Error: {e}")
