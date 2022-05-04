import telebot
from pytube import YouTube

bot = telebot.TeleBot("token")

DOWNLOAD_FOLDER = "E:/Video"

a = " "
video_obj = " "
stream = " "

@bot.message_handler(commands=['start', "help"])
def send_welcome(message):
	

	bot.send_message(message.chat.id, "Submit a link to a video on YouTube 😀. \nLike this, for example: https://www.youtube.com/watch?v=dQw4w9WgXсQ.")
	
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	global a
	global video_obj
	
	global stream 
	bot.send_message(message.chat.id, "Please, wait...")	
	video_obj = YouTube(message.text)
	stream = video_obj.streams.get_highest_resolution()
	stream.download(output_path=DOWNLOAD_FOLDER, filename='yt_video.mp4')
	video = open('E:/Video/yt_video.mp4', 'rb')
	bot.send_video(message.chat.id, video, timeout = 200)

bot.infinity_polling() 
