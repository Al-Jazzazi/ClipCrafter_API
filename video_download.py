import yt_dlp

def download_video(url, output_name):
    yt_opts = {
    'verbose': True,
    
    } 
    ydl = yt_dlp.YoutubeDL(yt_opts)
    ydl.download(url)

url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
download_video(url, "first video on yt" )


