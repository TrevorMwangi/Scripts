# pip install yt-dlp
# run code in terminal 
# copy-paste YT link 

import yt_dlp

url = input("Enter video URL: ")
output_directory = r"C:\Users\TREVOR\Videos\Captures"

ydl_opts = {
    'outtmpl': output_directory + '\\%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully!!")
