
def build_yt_dlp_options(codec: str, quality: str) -> dict:
    output_dict = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,
            'preferredquality': quality,
        }],
        # Hace la descarga mas resistente a microcortes de red.
        'retries': 20,
        'fragment_retries': 20,
        'retry_sleep_functions': {
            'http': lambda n: min(2 * n, 15),
            'fragment': lambda n: min(2 * n, 15),
        },
        'socket_timeout': 30,
        'continuedl': True,
        'concurrent_fragment_downloads': 1,
        'noprogress': False,
        'quiet': False,
        'no_warnings': False,

    }
    return output_dict

def build_download_options(max_attempts_per_url: int, retry_wait_seconds: int) -> dict:    
    options= {
        'max_attempts_per_url': max_attempts_per_url,
        'retry_wait_seconds': retry_wait_seconds
    }
    return options