import tkinter as tk
import youtube_dl
from urllib.parse import urlparse

root = tk.Tk()

root.geometry('350x300')
root.title("YouTube Downloader")
root.resizable(False, False)

var = tk.StringVar()

top_label = tk.Label(root, text="Enter URL:").pack()
url = tk.Entry(root, width=40, textvariable=var).pack()

def download():
    url_text = var.get()
    options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '200',
    }],
    #specify your own path if you want
    'outtmpl': 'songs/%(title)s.%(ext)s'
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url_text])

    

download_button = tk.Button(root, text="Download MP3", command=download).pack()

root.mainloop()