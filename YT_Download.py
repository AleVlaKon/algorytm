from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=wq3pr7qZbDU"  # замените на нужный URL
yt = YouTube(video_url)

stream = yt.streams.get_highest_resolution()  # выбирает видеопоток с наивысшим разрешением

output_path = "C:/Users/konti/Downloads"  # укажите путь для сохранения видео

stream.download(output_path)