# Use the Tkinter module
from tkinter import *

# Create the top-level (or root) window
root = Tk()
root.title('Wow Calculator')
root.geometry("680x200+100+100")

label = Label(root, text='hello world label')
label.pack()
# pack() It organizes the widgets in the block

# Other widgets
b1 = Button(root, text="hello button")
b1.pack()
scale = Scale(root, from_=0, to=10, orient=HORIZONTAL)
scale.pack()
ckbutton = Checkbutton(root, text="Checkbutton")
ckbutton.pack()
lbox = Listbox(root)
lbox.pack()

# wait for user interactions
mainloop()

###

# grid() It organizes the widgets in table-like structure
# place() It's used to place the widgets at a specific position you want