from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=20)

print(2,4,8)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=0, y=50)
my_label.grid(column=0, row=0)
my_label.config(padx=50,pady=10)

# my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    # my_label["text"] = "I got clicked"
    new_text = input.get()
    my_label.config(text=new_text)

#Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button2 = Button(text="new button", command=button_clicked)
button2.grid(column=3, row=0)

#input
input = Entry(width=10)
# input.pack()
input.grid(column=4, row=4)


window.mainloop()