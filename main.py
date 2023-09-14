from tkinter import *

BACKGROUND_COLOR = "#FBF0B2"
PINK = '#FFC7EA'
BLUE = '#CAEDFF'
PURPLE = '#D8B4F8'



################################ UI SETUP ################################
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')
card_img = PhotoImage(file='images/card_front.png')
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=2)
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card.create_image(400, 263, image=card_img)
card.grid(row=0, column=1, columnspan=2)
card.create_text(400, 263, text='中文')




window.mainloop()