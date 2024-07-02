import yt_dlp

def download_video(url):
    full_url = " https://www.youtube.com/" + url
    yt_opts = {
    'verbose': True,
    
    } 
    ydl = yt_dlp.YoutubeDL(yt_opts)
    ydl.download(full_url)

# url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
# download_video(url, "first video on yt" )


