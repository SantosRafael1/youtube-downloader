import youtube_dl
from urllib.parse import urlparse

url = str(input("URL: "))

#check if URL is valid or not
def valid_url(is_valid):
    provided_url = urlparse(url)
    if provided_url.netloc == "www.youtube.com" or provided_url.netloc == "youtu.be":
        return True
    else:
        return False

while valid_url(url) == False:
    print("Invalid URL. Please provide a valid URL")
    url = str(input("URL: "))


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '200',
    }],
    #specify your own path if you want
    'outtmpl': 'songs/%(title)s.%(ext)s'
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
