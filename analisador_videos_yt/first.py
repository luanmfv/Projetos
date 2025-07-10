import pytubefix
import ffmpeg
import openai

# Baixa o áudio do arquivo
import sys
url = sys.argv[1]
filename = 'audio.wav'
yt = pytubefix.YouTube(url)
stream = yt.streams[0].url
ffmpeg.input(stream).output(filename,
                             format='wav',
                                loglevel='error')

# Cria a transcrição
audio_file = open(filename, 'rb')
transcript = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio_file
).text

#Pede pela revisão
completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role': 'system',
         'content':'Você é um assistente de revisão de transcrições. Você irá revisar a transcrição do áudio e corrigir os erros de gramática, pontuação e ortografia. Você também irá formatar o texto para que fique mais legível. Você não irá alterar o conteúdo da transcrição, apenas corrigir os erros e formatar o texto.'},
        {'role': 'user',
         'content': f'Descreva o seguinte video: {transcript}'}
    ])

with open(f'resumo.md', 'w+') as md:
    md.write(completion.choices[0].message.content)
