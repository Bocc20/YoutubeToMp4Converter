import yt_dlp

def progress_hook(d):
    if d['status'] == 'downloading':
        downloaded_bytes = d.get('downloaded_bytes', 0)
        total_bytes = d.get('total_bytes', None)
        if total_bytes:
            percentage = (downloaded_bytes / total_bytes) * 100
            print(f"Download progress: {percentage:.2f}%")

def download_youtube_video(youtube_url, save_path):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  
            'progress_hooks': [progress_hook], 
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        print(f"Download complete! Video saved to {save_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    
    download_youtube_video(youtube_url)
