import youtube_dl

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
