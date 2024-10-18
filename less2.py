def correct_sentence(text):
    # text = text.capitalize()#Второе слово в любом случае будет маленькое, если даже оно было с большой буквы
    text = text[0].upper() + text[1:]#Если нужно, что-бы вторые слова не трогались
    if not text.endswith("."):
        text += "."

    print(text)

correct_sentence("greetings, friends")
correct_sentence("hello")
correct_sentence("Greetings. Friends")
correct_sentence("Greetings, friends.")
correct_sentence("greetings, friends.")

print('ОК')


