from tkinter import *

root = Tk()
root.geometry("400x400")

def show():
    day = inputday.get()
    month = inputmonth.get()
    label.config(text = f"Waktu saat ini: {day} {month}")
    
#Time Frame
frame = LabelFrame(root, text="Masukkan Waktu", padx=5, pady=5)
frame.pack()

# Create button, it will change label text
button = Button( frame , text = "Enter" , command = show ).grid(row=2,column=0)

# TextBox Creation
inputday = Text(frame, height = 1, width = 5)
inputmonth = Text(frame, height = 1, width = 5)
inputyear = Text(frame, height = 1, width = 5)

# Label Creation
label = Label(frame, text = "")


label.grid(row=2,column=2)
inputday.grid(row=0, column=0)
inputmonth.grid(row=0, column=2)
inputyear.grid(row=0, column=3)
root.mainloop()