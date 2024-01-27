from tkinter import *

window = Tk()
window.title("Mile To Km Converter")
# window.minsize(width=400,height=300)
window.config(padx=20, pady=20)

#Entery
mile_input = Entry(width=10,font=("Arial",20,"bold"))
mile_input.grid(column=1,row=0)

#label
mile_label = Label(text="Miles",font=("Arial",20,"bold"))
mile_label.grid(column=2,row=0)
mile_label.config(padx=10)

#label
comp_label = Label(text="is equal to",font=("Arial",20,"normal"))
comp_label.grid(column=0,row=1)

#label
output_label = Label(font=("Arial",20,"bold"))
output_label.grid(column=1,row=1)

#label
km_label = Label(text="Km",font=("Arial",20,"bold"))
km_label.grid(column=2,row=1)

def onclicked():
    ans_km = float(mile_input.get())*1.6
    output_label.config(text=round(ans_km,3))

#Button
button = Button(text="Calculate", command=onclicked,font=("Arial",20,"bold"))
button.grid(column=1,row=2)
button.config(bg="red", fg="white", borderwidth=2, relief="raised")

window.mainloop()