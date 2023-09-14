from tkinter import *
from PIL import ImageTk


BACKGROUND_COLOR = "#FBF0B2"
PINK = '#FFC7EA'
BLUE = '#CAEDFF'
PURPLE = '#D8B4F8'
FONT = 'Comic Sans MS'

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
encouraging_img = ImageTk.PhotoImage(file='images/study-motivation-quotes-4.jpg')
canvas = Canvas(width=600, height=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(300, 400, image=encouraging_img)
canvas.grid(row=0, column=1)


window.mainloop()