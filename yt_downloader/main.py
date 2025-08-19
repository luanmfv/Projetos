from pytubefix import YouTube
from pytube.cli import on_progress

url = 'https://www.youtube.com/watch?v=NpU_aN54eJA&list=RDNpU_aN54eJA&start_radio=1'
destino = 'yt_downloader/pasta_video'

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

# Tenta pegar 720p progressive (com áudio)
ys = yt.streams.filter(res="720p", progressive=True).first()

# Se não tiver progressive 720p, pega 720p DASH (vídeo sem áudio)
if not ys:
    ys = yt.streams.filter(res="720p", type="video").first()

if ys:
    ys.download(output_path=destino)
    print("Download concluído!")
else:
    print("Vídeo em 720p não disponível.")
