import os
import shutil
from yt_dlp import YoutubeDL
from utils import progress_hook

def download_audio(url: str, output_dir: str = ".", filename_template: str = "%(title)s.%(ext)s", audio_bitrate: str = "320K"):
    """ดาวน์โหลดออดิโอ ถ้ามี ffmpeg → แปลงเป็น mp3 คุณภาพสูง"""
    ffmpeg_installed = shutil.which("ffmpeg") is not None
    opts = {
        "outtmpl": os.path.join(output_dir, filename_template),
        "format": "bestaudio/best",
        "noplaylist": True,
        "quiet": False,
        "no_warnings": True,
        "progress_hooks": [progress_hook],
    }

    if ffmpeg_installed:
        opts["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": audio_bitrate.replace("K",""),
        }]
        print(f"ffmpeg detected → audio จะถูกแปลงเป็น mp3 {audio_bitrate}")
    else:
        print("ffmpeg ไม่พบ → ดาวน์โหลดไฟล์ audio ต้นฉบับ (.webm/.m4a)")

    with YoutubeDL(opts) as ydl:
        ydl.download([url])
