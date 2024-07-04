from moviepy.editor import VideoFileClip
import os

def video_to_audio(mp4_file, mp3_file): 
    try: 
        if not os.path.exists(mp4_file):
            print(f"Error: The video file '{mp4_file}' does not exist.")
            return
        
        video_clip = VideoFileClip(mp4_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()
        video_clip.close()
    except Exception as e:
        print(f"An error occurred: {e}") 

    

video_to_audio("123.mp4", "123.mp3")
