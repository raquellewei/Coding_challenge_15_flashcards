from tkinter import *
from tkinter import messagebox
from PIL.ImageTk import PhotoImage
from PIL import Image
import argparse
import json
import random

BACKGROUND_COLOR = "#FBF0B2"
PINK = '#FFC7EA'
BLUE = '#CAEDFF'
PURPLE = '#D8B4F8'
ENGLISH_FONT = 'Ariel'
CHINESE_FONT = 'Songti'
COUNT = 3000

########################################################################
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--developer', action='store_true')
args = parser.parse_args()

if args.developer:
    word_file = 'data/developer_list.json'
else:
    word_file = 'data/word_list.json'
def load_words():
    with open(word_file, 'r') as f:
        words = json.load(f)
    return words

words = load_words()

def next_word():
    global timer
    try:
        new_word = random.choice(list(words.keys()))
    except IndexError:
        messagebox.showinfo("Congratulations!", "You have mastered all the words.")
        window.destroy()
    else:
        window.after_cancel(timer)
        card.itemconfig(card_img, image=card_front)
        card.itemconfig(language, text='English', fill='black')
        card.itemconfig(word, text=new_word, fill='black')
        timer = window.after(COUNT, flip)


def flip():
    card.itemconfig(card_img, image=card_back)
    card.itemconfig(language, text="Chinese", fill='white')
    current_word = card.itemcget(word, "text")
    card.itemconfig(word, text=words[current_word], fill='white')


def yes():
    current_word = card.itemcget(word, "text")
    if current_word in words:
        del words[current_word]
    next_word()


################################ UI SETUP ################################
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

right_img = Image.open('images/my_tick.jpg')
right_img = right_img.resize((100, 100))
right_img = PhotoImage(right_img)
wrong_img = Image.open('images/my_cross.jpg')
wrong_img = wrong_img.resize((100, 100))
wrong_img = PhotoImage(wrong_img)

card_front = PhotoImage(file='images/my_card_front.png')
card_back = PhotoImage(file='images/my_card_back.png')
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=yes)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=next_word)
wrong_button.grid(row=1, column=2)

card = Canvas(width=500, height=310, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = card.create_image(250, 160, image=card_front)
language = card.create_text(250, 100, text="", font=(ENGLISH_FONT, 40, 'italic'), fill='black')
word = card.create_text(250, 190, text="", fill='black', font=(CHINESE_FONT, 60, "bold"))
card.grid(row=0, column=1, columnspan=2)

timer = window.after(COUNT, flip)
next_word()

window.mainloop()