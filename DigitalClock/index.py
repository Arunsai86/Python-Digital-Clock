from tkinter import Label, Tk
from time import strftime

main_root = Tk()
main_root.title("Digital Clock")
main_root.resizable(1,1)

label = Label(main_root, font=("Helvetica", 60, 'bold'), bg="#000000", fg="#ffffff", bd=50)
label.grid(row=2, column=1)


def digital_clock():
   time_live = strftime("%H:%M:%S %d %B, %Y")
   label.config(text=time_live,)
   label.pack(anchor="center")
   label.after(200, digital_clock)

digital_clock()

main_root.mainloop()
