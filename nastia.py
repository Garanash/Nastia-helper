from gtts import gTTS
from googletrans import Translator
import os
import subprocess


def with_translate(text):
    obj = gTTS(text, lang='en')
    obj.save('test1.wav')
    subprocess.call(["afplay", audio_file])


def without_translate(text):
    translation = translator.translate(text, dest='ru')
    obj = gTTS(translation.text, lang='ru')
    obj.save('test1.wav')
    subprocess.call(["afplay", audio_file])


spisok_pogovorok = ['Easy Peasy', 'East or West home is best',
                    'Better late than never ', 'A penny saved is a penny gained',
                    'All’s well that ends well', 'Out of sight out of mind']

obj = gTTS('Привет! я голосовой помощник Настя. '
           'Сейчас я переведу тебе парочку английских поговорок)', lang='ru')
obj.save('test1.wav')
audio_file = os.path.expanduser("~/Desktop/sfgdhfgj/test1.wav")
return_code = subprocess.call(["afplay", audio_file])

translator = Translator()
for text in spisok_pogovorok:
    with_translate(text)
    without_translate(text)
