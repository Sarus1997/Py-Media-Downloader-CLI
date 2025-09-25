import os
from yt_dlp import YoutubeDL
from utils import progress_hook

def download_video(url: str, output_dir: str = ".", filename_template: str = "%(title)s.%(ext)s"):
    """ดาวน์โหลดวิดีโอความคมชัดสูงสุดและรวมเป็น MP4"""
    opts = {
        "outtmpl": os.path.join(output_dir, filename_template),
        "format": "best",  # ดาวน์โหลดไฟล์เดียว (รวม audio+video หรือไฟล์ mp4)
        "noplaylist": True,
        "quiet": False,
        "no_warnings": True,
        "progress_hooks": [progress_hook],
    }

    with YoutubeDL(opts) as ydl:
        ydl.download([url])
