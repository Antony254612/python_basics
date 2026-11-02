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
    ydl.download(['https://youtu.be/-bNwqXvMuB8?si=GHY9bpKLC4-q88bq'])