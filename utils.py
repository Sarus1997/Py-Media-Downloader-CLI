import sys

def human_readable(n):
    for unit in ['B','KB','MB','GB','TB']:
        if n < 1024.0:
            return f"{n:3.1f}{unit}"
        n /= 1024.0
    return f"{n:.1f}PB"

def progress_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        if total:
            pct = downloaded / total * 100
            sys.stdout.write(f"\rDownloading: {pct:.1f}% ({human_readable(downloaded)} / {human_readable(total)})")
        else:
            sys.stdout.write(f"\rDownloading: {human_readable(downloaded)}")
        sys.stdout.flush()
    elif d['status'] == 'finished':
        print("\nDownload finished!")
