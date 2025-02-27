from tkinter import *

root = Tk()
root.geometry("680x200+100+100")

# redbutton = Button(root, text="left", fg="red")
# redbutton.pack(side=LEFT)
#
# greenbutton = Button(root, text="right", fg="green")
# greenbutton.pack(side=RIGHT)
#
# bluebutton = Button(root, text="top", fg="blue")
# bluebutton.pack(side=TOP)
#
# blackbutton = Button(root, text="bottom", fg="black")
# blackbutton.pack(side=BOTTOM)

# Layout using Grid

label = Label(root, text="hello world label")
label.grid(row=0, column=0)

b1 = Button(root, text="hello button")
b1.grid(row=0, column=1)
scale = Scale(root, from_=0, to=10, orient=HORIZONTAL)
scale.grid(row=1, column=0)
ckbutton = Checkbutton(root, text="Checkbutton")
ckbutton.grid(row=1, column=1)
lbox = Listbox(root)
lbox.grid(row=2, column=0, columnspan=2)

root.mainloop()

# Use pack() for simple layouts !

# from tkinter import *
# root = Tk()
# for i in range(5):
#   Label(root, text=str(i), relief=GROOVE).pack(fill=BOTH, expand=True)
# for i in range(5):
#   Label(root, text=str(i), relief=GROOVE).pack(side=RIGHT, fill=BOTH, expand=True)
# for i in range(5):
#   Label(root, text=str(i), relief=GROOVE).pack(side=BOTTOM, fill=BOTH, expand=True)
# for i in range(5):
#  Label(root, text=str(i), relief=GROOVE).pack(side=LEFT,fill=BOTH, expand=True)
# root.mainloop()