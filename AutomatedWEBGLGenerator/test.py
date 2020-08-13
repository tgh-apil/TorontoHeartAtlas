from tkinter import *

root = Tk()

class Flash_Card(object):
    def __init__(self, side_1):
        self.side_1 = side_1

test_card = Flash_Card("line3\\\\nline4")

def changeLabel():
    test_label.config(text = test_card.side_1)

test_label = Label(root, text = "Hello, World!")
test_button = Button(root, text = "Change label", command = changeLabel)

test_label.pack()
test_button.pack()

root.mainloop()