from pytubefix import YouTube
from pytube.cli import on_progress
import subprocess
import os

url = str(input('Digite a url:'))
destino = 'yt_downloader/pasta_video'

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

# Baixa vídeo 720p (DASH, sem áudio)
video_stream = yt.streams.filter(res="720p", type="video").first()
# Baixa áudio separado
audio_stream = yt.streams.filter(only_audio=True).first()

video_path = os.path.join(destino, "video.mp4")
audio_path = os.path.join(destino, "audio.mp4")
final_path = os.path.join(destino, f"{yt.title}.mp4")

video_stream.download(output_path=destino, filename="video.mp4")
audio_stream.download(output_path=destino, filename="audio.mp4")

# Junta vídeo e áudio com ffmpeg
subprocess.run([
    "ffmpeg", "-y", "-i", video_path, "-i", audio_path,
    "-c:v", "copy", "-c:a", "aac", final_path
])

# Remove arquivos temporários
os.remove(video_path)
os.remove(audio_path)

print("Download 720p com áudio concluído!")
