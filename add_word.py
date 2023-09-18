from tkinter import *
from PIL import ImageTk, Image
import json
import argparse


#BACKGROUND_COLOR = "#FBF0B2"
PINK = '#FFC7EA'
BLUE = '#CAEDFF'
PURPLE = '#D8B4F8'
FONT = 'Comic Sans MS'
BACKGROUND_COLOR = BLUE

# add word
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--developer', action='store_true')
args = parser.parse_args()
if args.developer:
    word_file = 'data/developer_list.json'
else:
    word_file = 'data/word_list.json'
def add_word():
    new_word = new_word_box.get()
    meaning = translation_box.get()
    new_data = {new_word: meaning}
    try:
        with open(word_file, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(word_file, 'w') as f:
            json.dump(new_data, f, indent=4)
    else:
        data.update(new_data)
        with open(word_file, 'w') as f:
            json.dump(data, f, indent=4)
    finally:
        new_word_box.delete(0, END)
        translation_box.delete(0, END)




# UI Setup
window = Tk()
window.title("Add a word!")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

new_word_label = Label(text="New word: ", font=(FONT, 15, 'normal'), bg=BACKGROUND_COLOR)
new_word_label.grid(row=1, column=0)
new_word_box = Entry(highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
new_word_box.grid(row=1, column=1)
new_word_box.focus()
translation_text = Label(text="Translation: ", font=(FONT, 15, 'normal'), bg=BACKGROUND_COLOR)
translation_text.grid(row=2, column=0)
translation_box = Entry(highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
translation_box.grid(row=2, column=1)
add_button = Button(text="Add", borderwidth=0.5, highlightbackground=BACKGROUND_COLOR, font=(FONT, 15, 'normal'),
                    command=add_word)
add_button.grid(row=3, column=0, columnspan=2, sticky="EW")
encouraging_img = Image.open('images/foreign_lang.jpeg')
encouraging_img = encouraging_img.resize((418, 279))
encouraging_img = ImageTk.PhotoImage(encouraging_img)
canvas = Canvas(width=418, height=279, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(209, 139.5, image=encouraging_img)
canvas.grid(row=0, column=0, columnspan=2)









window.mainloop()