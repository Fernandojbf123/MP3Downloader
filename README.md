
# MP3Downloader (ESPAÑOL / ENGLISH [DOWN BELOW])
## Descargar mp3 desde YouTube utilizando la librería yt-dlp y FFmpeg

### Instrucciones paso a paso
1. **Abre una terminal en la carpeta del proyecto.**

2. **Instala uv (si no lo tienes instalado):**
    ```powershell
    pip install uv
    ```
    `uv` es el manejador de paquetes utilizado en este proyecto.

3. **Crea el ambiente virtual e instala las dependencias:**
    ```powershell
    uv sync
    ```
    Este comando crea automáticamente el ambiente virtual `.venv` e instala todas las dependencias necesarias.

4. **Activa el ambiente virtual:**
    ```powershell
    .venv\Scripts\activate
    ```
    (En PowerShell o CMD, dentro de la carpeta del proyecto)


5. **Instala FFmpeg:**
    Ejecuta el siguiente comando en una terminal de Windows (PowerShell o CMD):
    ```powershell
    winget install "FFmpeg (Essentials Build)"
    ```

6. **Agrega FFmpeg a la variable de entorno PATH (si es necesario):**
    Si al ejecutar el programa aparece un error indicando que no se encuentra FFmpeg o ffprobe, sigue estos pasos:
    1. Ubica la carpeta donde está instalado FFmpeg. Por ejemplo:
        - `C:\Program Files\ffmpeg\bin`
        - O una ruta similar en tu carpeta de usuario, dependiendo de cómo se instaló.
    2. Copia la ruta completa de la carpeta `bin`.
    3. Abre el Panel de Control → Sistema → Configuración avanzada del sistema → Variables de entorno.
    4. En "Variables del sistema", selecciona la variable llamada `Path` y haz clic en "Editar".
    5. Haz clic en "Nuevo" y pega la ruta copiada.
    6. Acepta todos los cambios y cierra las ventanas.
    7. Cierra y vuelve a abrir la terminal para que los cambios surtan efecto.
    8. Verifica que FFmpeg está disponible ejecutando:
        ```powershell
        ffmpeg -version
        ```
    Si ves información de FFmpeg, ya está correctamente configurado.

7. **(Opcional)** Si tienes problemas para ejecutar yt-dlp, asegúrate de que la ruta de yt-dlp esté incluida en la variable de entorno `PATH` de tu sistema.

[Imagen de ayuda 1](help_addpath_1.png)

[Imagen de ayuda 2](help_addpath_2.png)

[Imagen de ayuda 3](help_addpath_3.png)


8. **Ejecuta el programa:**
    ```powershell
    python main.py
    ```

7. **Ejecuta el programa:**
    ```powershell
    python main.py
    ```

#### Información sobre las variables
[helpme.md](helpme.md)

#### NOTA: Versión de python recomendada 3.14
#### SOLO PARA FINES EDUCATIVOS. NO USAR PARA FINES COMERCIALES
#### USO BAJO RESPONSABILIDAD PROPIA SI NO TIENES LAS LICENCIAS NI LOS DERECHOS SOBRE LAS CANCIONES.
---


# MP3Downloader (SPANISH / ENGLISH [DOWN BELOW])
## Download mp3 from YouTube using the yt-dlp library and FFmpeg
### Step-by-step instructions
1. **Open a terminal in the project folder.**
2. **Install uv (if not already installed):**
    ```powershell
    pip install uv
    ```
    `uv` is the package manager used in this project.
3. **Create the virtual environment and install dependencies:**
    ```powershell
    uv sync
    ```
    This command automatically creates the `.venv` virtual environment and installs all required dependencies.
4. **Activate the virtual environment:**
    ```powershell
    .venv\Scripts\activate
    ```
    (In PowerShell or CMD, inside the project folder)

5. **Install FFmpeg:**
    Run the following command in a Windows terminal (PowerShell or CMD):
```powershell
winget install “FFmpeg (Essentials Build)”
```
6. **Add FFmpeg to the PATH environment variable (if necessary):**
    If an error appears when running the program indicating that FFmpeg or ffprobe cannot be found, follow these steps:
1. Locate the folder where FFmpeg is installed. For example:
- `C:\Program Files\ffmpeg\bin`
- Or a similar path in your user folder, depending on how it was installed.
    2. Copy the full path of the `bin` folder.
3. Open Control Panel → System → Advanced system settings → Environment Variables.
4. Under “System variables,” select the variable called `Path` and click “Edit.”
5. Click “New” and paste the copied path.
6. Accept all changes and close the windows.
7. Close and reopen the terminal for the changes to take effect.
8. Verify that FFmpeg is available by running:
```powershell
ffmpeg -version
```
If you see FFmpeg information, it is already correctly configured.
7. **(Optional)** If you have trouble running yt-dlp, make sure the path to yt-dlp is included in your system's `PATH` environment variable.

[Support image 1](help_addpath_1.png)

[Support image 2](help_addpath_2.png)

[Support image 3](help_addpath_3.png)

8. **Run the program:**
```powershell
python main.py
```
7. **Run the program:**
```powershell
python main.py
```
#### Information about variables
[helpme.md](helpme.md)
#### NOTE: Recommended Python version 3.14
#### FOR EDUCATIONAL PURPOSES ONLY. DO NOT USE FOR COMMERCIAL PURPOSES.
#### USE AT YOUR OWN RISK IF YOU DO NOT HAVE THE LICENSES OR RIGHTS TO THE SONGS.
---