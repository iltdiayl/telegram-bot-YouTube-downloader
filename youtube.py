from pytube import YouTube

DOWNLOAD_FOLDER = "C:/Users/Abzal/Desktop/YouTube"

a = input("Введите ссылку: ")

video_obj = YouTube(a)
   

stream = video_obj.streams.get_highest_resolution()

stream.download(DOWNLOAD_FOLDER)