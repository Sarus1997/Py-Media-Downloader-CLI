# Media Downloader CLI

### โปรเจกต์ Python สำหรับดาวน์โหลดวิดีโอและออดิโอจากเว็บไซต์ต่าง ๆ ด้วย `yt-dlp`   รองรับการดาวน์โหลดคุณภาพสูง และสามารถแปลงไฟล์ออดิโอเป็น MP3 ได้ถ้ามี `ffmpeg` ติดตั้งอยู่ในระบบ

## คุณสมบัติ

- ดาวน์โหลดวิดีโอความคมชัดสูงสุด พร้อม audio รวมเป็นไฟล์ MP4  
- ดาวน์โหลดไฟล์ออดิโอคุณภาพสูงสุด พร้อมแปลงเป็น MP3 (ถ้ามี ffmpeg)  
- แสดงความคืบหน้าของการดาวน์โหลดแบบเรียลไทม์  
- รองรับการดาวน์โหลดไฟล์เดี่ยว ไม่รวม playlist  

---

## การติดตั้ง

1. Clone โปรเจกต์นี้
```bash
git clone https://github.com/Sarus1997/py-media-downloader-cli

cd py-media-downloader-cli
```

2. ติดตั้ง dependencies

```bash
pip install -r requirements.txt
```

  - หรือ ติดตั้ง `yt-dlp` ด้วยคำสั่ง

```bash
python -m pip install -U yt-dlp
```

### การตรวจสอบ yt-dlp รายละเอียดการรองรับ โดยใช้คําสั่ง

```bash
yt-dlp --list-extractors 
```

### ตัวอย่างเว็บไซต์ยอดนิยมที่ yt-dlp รองรับ
- YouTube (รวมทั้ง playlist, channel, livestreams)
- Facebook (วิดีโอแบบ public)
- Instagram (reels, videos, stories)
- TikTok
- Twitter / X (วิดีโอและ GIF)
- SoundCloud
- Vimeo
- Twitch (VOD, livestreams)
- Bilibili
- DailyMotion

### ถ้าอยากเช็คเว็บใดเว็บหนึ่ง เช่น youtube หรือ tiktok:

```bash
yt-dlp --list-extractors | grep youtube
yt-dlp --list-extractors | grep tiktok
```

3. ติดตั้ง ffmpeg สำหรับคุณภาพสูง (ไม่บังคับ) 

- Windows: ดาวน์โหลด ffmpeg
- macOS: brew install ffmpeg
- Linux: ใช้ apt install ffmpeg หรือแพ็กเกจที่เหมาะสม

---

## ตัวอย่างการใช้งาน

### แก้ไขไฟล์ `main.py` เพื่อกำหนด URL และโหมดการดาวน์โหลด

```python
URL = "https://youtu.be/nsKpUnkjWTE?si=YhJ2YVinoMF5zNBk"
MODE = "audio"  # หรือ "video"
OUTPUT_DIR = "downloads"
AUDIO_BITRATE = "320K"  # ใช้เฉพาะ MODE="audio"
```

### รันโปรเจกต์

```bash
python main.py
```

- โหมด video → ดาวน์โหลดไฟล์ MP4
- โหมด audio → ดาวน์โหลดไฟล์ audio 

** ถ้ามี ffmpeg จะได้คุณภาพสูงสุด ** 

| ตัวแปร        | คำอธิบาย                                    | ค่าเริ่มต้น   |
| ------------- | ------------------------------------------- | ------------- |
| URL           | ลิงก์ YouTube ที่ต้องการดาวน์โหลด           | `-`             |
| MODE          | เลือกโหมดดาวน์โหลด `"video"` หรือ `"audio"` | `"audio"`     |
| OUTPUT_DIR    | โฟลเดอร์สำหรับบันทึกไฟล์                    | `"downloads"` |
| AUDIO_BITRATE | คุณภาพไฟล์ MP3 (kbps)                       | `"320K"`      |


## หมายเหตุ: 

- ถ้า ไม่มี ffmpeg → audio จะถูกดาวน์โหลดเป็นไฟล์ต้นฉบับ (.webm/.m4a)
- โปรแกรมนี้ ไม่รองรับ playlist
- การดาวน์โหลดขึ้นอยู่กับข้อกำหนดและนโยบายของแต่ละเว็บไซต์

## ข้อมูลเพิ่มเติม:

- `__pycache__` เป็นโฟลเดอร์ที่ Python สร้างขึ้นเพื่อเก็บ ไฟล์ bytecode (.pyc)
- ไฟล์เหล่านี้ช่วยให้ Python รันเร็วขึ้น แต่ ไม่จำเป็นสำหรับการแชร์หรือเก็บใน Git
- การเก็บไว้ใน repo จะทำให้ repo มีขนาดใหญ่ขึ้นโดยไม่จำเป็น
- ควรลบ `__pycache__` เมื่อใช้งานเสร็จสมบูรณ์ เพื่อประหยัดหน่วยความจํา ดังนั้น แม้คุณลบ __pycache__ แล้ว ถ้ารันสคริปต์ Python อีกครั้ง Python จะสร้างโฟลเดอร์และไฟล์ .pyc ใหม่ทันที

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
