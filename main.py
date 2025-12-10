# Configs
codec = 'mp3' # "mp3" "mp4"
quality = '192' # kbps for mp3

### Links ###
urls = ["https://www.youtube.com/watch?v=flLIohkevQI"]

# Ver detalles en: [helpme.md](helpme.md)


## NO TOCAR // DO NOT TOUCH ##
import yt_dlp
options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': codec,
        'preferredquality': quality,
    }],
}

with yt_dlp.YoutubeDL(options) as ydl:
    for url in urls:
        ydl.download([url])