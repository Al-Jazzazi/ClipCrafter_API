import yt_dlp

def download_video(url, output_name):
    ydl_opts = {'outtmpl': output_name}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
