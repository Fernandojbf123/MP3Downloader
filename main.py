from src.download_manager import *
# Configs
codec = 'mp3' # "mp3" "mp4"
quality = '192' # kbps for mp3

### Links ###
urls = ["https://www.youtube.com/watch?v=ue5OgiUists"]


# Ver detalles en: [helpme.md](helpme.md)
download_manager(codec= codec, quality=quality, urls=urls)

