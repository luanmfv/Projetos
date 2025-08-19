from pytubefix import YouTube #importando a classe YouTube do pytubefix
from pytube.cli import on_progress # para ver o progresso do download

url = 'https://www.youtube.com/watch?v=NpU_aN54eJA&list=RDNpU_aN54eJA&start_radio=1'

destino = 'yt_downloader/pasta_video'

yt = YouTube(url, on_progress_callback=on_progress) #instanciando a classe YouTube com a url e o callback de progresso
print(yt.title) #imprimindo o título do vídeo

ys = yt.streams.get_highest_resolution() #pegando o stream com a maior resolução
ys.download(output_path=destino) #fazendo o download do vídeo para o destino especificado

