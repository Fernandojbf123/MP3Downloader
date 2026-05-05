## NO TOCAR // DO NOT TOUCH ##

from src.download_with_retry import download_with_retries
from src.build_options import *

def download_manager(codec: str, quality: str, urls: list):
    """
        Handles the download process for a list of URLs, using yt-dlp with retry logic for robustness against network issues.
        Args:
            codec (str): The desired audio codec (e.g., 'mp3', 'mp4').
            quality (str): The desired audio quality (e.g., '192' for kbps).
            urls (list): A list of URLs to download.
    """
    max_attempts_per_url = 3  # Reintentos por URL cuando hay cortes de red
    retry_wait_seconds = 5 # Segundos a esperar entre reintentos

    yt_dlp_options = build_yt_dlp_options(codec = codec, 
                            quality = quality)

    download_options = build_download_options(max_attempts_per_url = max_attempts_per_url, 
                                            retry_wait_seconds = retry_wait_seconds)

    failed_urls = []
    for url in urls:
        success = download_with_retries(yt_dlp_options, download_options, url)
        if not success:
            failed_urls.append(url)

    if failed_urls:
        print('\nDescargas con error:')
        for item in failed_urls:
            print(f'- {item}')
    else:
        print('\nTodas las descargas finalizaron correctamente.')