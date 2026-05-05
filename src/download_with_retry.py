import yt_dlp
import time
from yt_dlp.utils import DownloadError

def download_with_retries(yt_dlp_options: dict, download_options: dict, url: str) -> bool:
    max_attempts_per_url = download_options.get('max_attempts_per_url', 3)
    retry_wait_seconds = download_options.get('retry_wait_seconds', 5)
    
    for attempt in range(1, max_attempts_per_url + 1):
        try:
            with yt_dlp.YoutubeDL(yt_dlp_options) as ydl:
                ydl.download([url])
            print(f'OK: descarga completada -> {url}')
            return True
        except KeyboardInterrupt as exc:
            # Algunos fallos de red terminan propagados como KeyboardInterrupt en Windows.
            if attempt == max_attempts_per_url:
                print(f'ERROR: descarga interrumpida tras {attempt} intentos -> {url}')
                print(f'Detalle: {exc}')
                return False
            print(f'RETRY {attempt}/{max_attempts_per_url}: interrupcion detectada, reintentando en {retry_wait_seconds}s...')
            time.sleep(retry_wait_seconds)
        except DownloadError as exc:
            if attempt == max_attempts_per_url:
                print(f'ERROR: no se pudo descargar tras {attempt} intentos -> {url}')
                print(f'Detalle: {exc}')
                return False
            print(f'RETRY {attempt}/{max_attempts_per_url}: error de descarga, reintentando en {retry_wait_seconds}s...')
            time.sleep(retry_wait_seconds)
        except Exception as exc:
            if attempt == max_attempts_per_url:
                print(f'ERROR: fallo inesperado tras {attempt} intentos -> {url}')
                print(f'Detalle: {exc}')
                return False
            print(f'RETRY {attempt}/{max_attempts_per_url}: error inesperado, reintentando en {retry_wait_seconds}s...')
            time.sleep(retry_wait_seconds)

    return False