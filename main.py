import os
from video_downloader import download_video
from audio_downloader import download_audio

# ----------------------------
URL = "https://youtu.be/gM7BmLsJFW0?si=R8sewDhs8UCFxJAE"
MODE = "video"  # "video" หรือ "audio"
OUTPUT_DIR = "downloads"
AUDIO_BITRATE = "320K"  # ใช้เมื่อ MODE="audio"
# ----------------------------

os.makedirs(OUTPUT_DIR, exist_ok=True)

try:
    if MODE == "video":
        download_video(URL, output_dir=OUTPUT_DIR)
    else:
        download_audio(URL, output_dir=OUTPUT_DIR, audio_bitrate=AUDIO_BITRATE)
except Exception as e:
    print("Error:", e)
