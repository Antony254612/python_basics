import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',

        }
    ],
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
  ydl.download(['https://youtu.be/QYh6mYIJG2Y?si=wrK4pF2D-4I_Uyuw'])