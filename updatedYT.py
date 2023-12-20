# pip install pytube
# pip install tqdm
# pip install colorama

from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm
import requests
import os

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()

        print("Downloading...")
        response = requests.get(highest_res_stream.url, stream=True)
        total_size = int(response.headers.get('content-length', 0))

        file_name = f"{yt.title}.mp4"
        file_path = os.path.join(save_path, file_name)

        with open(file_path, 'wb') as file, tqdm(
                desc=f"{file_name} - {total_size / (1024 * 1024):.2f} MB",
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                miniters=1,
                ncols=140  # Set the width of the progress bar
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)

        print("\nVideo downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    try:
        folder = filedialog.askdirectory()
        if folder:
            print(f"Selected folder: {folder}")
            return folder
        else:
            print("Folder selection canceled. Using the current working directory.")
            return ""
    except Exception as e:
        print(f"An error occurred: {e}. Using the current working directory.")
        return ""

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
