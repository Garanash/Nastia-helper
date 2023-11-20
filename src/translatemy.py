from gtts import gTTS
from googletrans import Translator
#import pygame
import os
import subprocess


def without_translate(text):
    obj = gTTS(text, lang='ru')
    obj.save('test1.wav')
    subprocess.call(["afplay", audio_file])


def with_translate(text):
    translation = translator.translate(text, dest='en')
    obj = gTTS(translation.text, lang='en')
    obj.save('test1.wav')
    subprocess.call(["afplay", audio_file])


spisok_pogovorok = ['Easy Peasy', 'East or West home is best',
                    'Better late than never ', 'A penny saved is a penny gained',
                    'All’s well that ends well', 'Out of sight out of mind']


obj = gTTS('Привет! я голосовой помощник Настя. я ничего не умею), помогите мне развиться, поговорите со мной', lang='ru')
obj.save('test1.wav')
audio_file = os.path.expanduser("~/Desktop/sfgdhfgj/test1.wav")
return_code = subprocess.call(["afplay", audio_file])

translator = Translator()
# for text in spisok_pogovorok:
#     with_translate(text)
#     without_translate(text)
