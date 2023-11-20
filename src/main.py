import translatemy
import recogn

recogn.zapis()
user_text = recogn.raspoznovanie('output.wav')
print(user_text)
if 'андрей' in user_text.lower():
    translatemy.without_translate('Да Андрей лучший человек в мире')
elif 'сан саныч' in user_text.lower():
    translatemy.without_translate('Да да, знаю этого мордвина')
elif 'переведи' in user_text.lower():
    ind = user_text.lower().find("переведи")
    ind += 8
    translatemy.with_translate(user_text[ind:])
else:
    translatemy.without_translate('Пожалуй вы правы')