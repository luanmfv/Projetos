from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print('Download completed!')

url = input("Enter the YouTube video URL: ")
download_video(url)
