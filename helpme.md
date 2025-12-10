# helpme.md

## Explicación de variables en main.py

### 1. Variable `codec`
- **¿Qué es?**
  - La variable `codec` define el formato de archivo de audio que se generará al descargar el video de YouTube.
- **Opciones recomendadas:**
  - `mp3`: Genera un archivo de audio en formato MP3.
  - `mp4`: Genera un archivo de audio en formato MP4 (AAC).
- **Uso:**
  - Cambia el valor de la variable `codec` a `mp3` o `mp4` según el formato de salida que desees.

### 2. Variable `quality`
- **¿Qué es?**
  - La variable `quality` determina la calidad del archivo de audio de salida, expresada en kbps (kilobits por segundo).
- **Valores recomendados:**
  - `128`: Calidad estándar, tamaño de archivo más pequeño.
  - `192`: Mejor calidad, tamaño de archivo mayor.
- **Uso:**
  - Cambia el valor de la variable `quality` a `128` o `192` según la calidad de audio que prefieras.

### 3. Variable `urls`
- **¿Qué es?**
  - La variable `urls` es una lista que contiene los enlaces de YouTube que deseas descargar.
- **Uso:**
  - Agrega uno o más enlaces de YouTube dentro de la lista, por ejemplo:
    ```python
    urls = [
        "https://www.youtube.com/watch?v=flLIohkevQI",
        "https://www.youtube.com/watch?v=otro_enlace"
    ]
    ```
