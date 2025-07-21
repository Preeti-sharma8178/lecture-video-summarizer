import streamlit as st
from transcribe import transcribe_audio
from summarize_ml import summarize_text
from scene_detect import detect_scenes
from rank_clips import rank_clips
import os

st.title("🎥 AI-Powered Lecture Video Summarizer")

uploaded_file = st.file_uploader("Upload a Lecture Video", type=["mp4", "mkv"])

if uploaded_file:
    video_path = f"uploads/{uploaded_file.name}"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    st.info("📌 Step 1: Transcribing Audio...")
    transcript = transcribe_audio(video_path)
    st.success("Transcription Complete ✅")

    st.info("📌 Step 2: Generating Summary...")
    summary = summarize_text(transcript)
    st.success("Summary Ready ✅")
    st.text_area("📄 Summary", summary, height=300)

    st.info("📌 Step 3: Detecting Scenes...")
    scenes = detect_scenes(video_path)
    st.write(f"🔍 Detected {len(scenes)} scene changes.")

    # Optional: show top sentences relevant to summary
    segments = transcript.split(".")
    top_segments = rank_clips(segments, summary)
    st.write("🔑 Top Transcript Segments Related to Summary:")
    for score, seg in top_segments:
        st.write("-", seg.strip())

