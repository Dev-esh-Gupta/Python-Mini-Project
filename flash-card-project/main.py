from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# ----------- Data Fetching --------------#


data_dict = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text= "French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=flash_card_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=flash_card_new_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    data_dict.remove(current_card)
    print(len(data_dict))
    updated_data = pandas.DataFrame(data_dict)
    updated_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# ---------- UI SETUP ------------------- #


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
flash_card_img = PhotoImage(file='./images/card_front.png')
flash_card_new_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400,264,image=flash_card_img)
card_title = canvas.create_text(400,150,text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263,text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
right_img = PhotoImage(file="./images/right.png")
known_button = Button(image=right_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()


window.mainloop()
