from tkinter import *
from PIL.ImageTk import PhotoImage
from PIL import Image

BACKGROUND_COLOR = "#FBF0B2"
PINK = '#FFC7EA'
BLUE = '#CAEDFF'
PURPLE = '#D8B4F8'

################################ UI SETUP ################################
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

right_img = Image.open('images/blue_tick.jpg')
right_img = right_img.resize((100, 100))
right_img = PhotoImage(right_img)
wrong_img = Image.open('images/pink_cross.jpg')
wrong_img = wrong_img.resize((100, 100))
wrong_img = PhotoImage(wrong_img)

card_img = PhotoImage(file='images/card_front.jpg')
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, relief='flat')
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0)
wrong_button.grid(row=1, column=2)

card = Canvas(width=800, height=558, bg=BACKGROUND_COLOR, highlightthickness=0)
card.create_image(400, 279, image=card_img)
card.create_text(400, 279, text='中文', fill='black')
card.grid(row=0, column=1, columnspan=2)




window.mainloop()