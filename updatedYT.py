from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import requests
from tqdm import tqdm

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        
        video_url = highest_res_stream.url
        response = requests.get(video_url, stream=True)
        
        # Get video size
        total_size = int(response.headers.get('content-length', 0))
        
        # Set up progress bar
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024)

        with open(save_path, 'wb') as f:
            for data in response.iter_content(chunk_size=1024):
                f.write(data)
                progress_bar.update(len(data))

        # Close the progress bar after download completion
        progress_bar.close()

        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir + "/video.mp4")  # Change the file name if needed
    else:
        print("Invalid save location.")
