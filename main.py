import yt_dlp

urls = ["https://www.youtube.com/watch?v=flLIohkevQI"]

options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(options) as ydl:
    for url in urls:
        ydl.download([url])