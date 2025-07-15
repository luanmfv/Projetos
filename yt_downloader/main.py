import yt_dlp

url = 'https://www.youtube.com/watch?v=AfMKqEn4Jes'

ydl_opts = {
    'format': 'bestaudio/best',  # só áudio (melhor disponível)
    'outtmpl': '%(title)s_audio.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
