from tkinter import *
from PIL import ImageTk, Image
import json


#BACKGROUND_COLOR = "#FBF0B2"
PINK = '#FFC7EA'
BLUE = '#CAEDFF'
PURPLE = '#D8B4F8'
FONT = 'Comic Sans MS'
BACKGROUND_COLOR = BLUE

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
add_button = Button(text="Add", borderwidth=0.5, highlightbackground=BACKGROUND_COLOR, font=(FONT, 15, 'normal'))
add_button.grid(row=3, column=0, columnspan=2, sticky="EW")
encouraging_img = Image.open('images/foreign_lang.jpeg')
encouraging_img = encouraging_img.resize((418, 279))
encouraging_img = ImageTk.PhotoImage(encouraging_img)
canvas = Canvas(width=418, height=279, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(209, 139.5, image=encouraging_img)
canvas.grid(row=0, column=0, columnspan=2)

# Add word #
word_list = 'data/word_list.json'
def add():
    new_word = new_word_box.get()
    meaning = translation_box.get()
    new_data = {new_word: meaning}




window.mainloop()