import pyperclip

txt = pyperclip.paste()
english_letters = list("qwertyuiopasdfghjkl;zxcvbnm,.")
hebrew_letters = list("/'קראטוןםפשדגכעיחלךףזסבהנמצתץ")
new_txt = []
for letter in txt:
    if letter in english_letters:
        index = english_letters.index(letter)
        new_txt.append(hebrew_letters[index])
    if letter in hebrew_letters:
        index = hebrew_letters.index(letter)
        new_txt.append(english_letters[index])
    else:
        new_txt.append(letter)

new_txt = "".join(new_txt)
pyperclip.copy(new_txt)
