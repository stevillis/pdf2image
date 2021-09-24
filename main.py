import os
from datetime import datetime
from tkinter import *
from tkinter import messagebox

from pdf2image import convert_from_path


def pdf2img():
    try:
        path = str(entry.get())
        path_to_save, filename = os.path.split(path)

        images = convert_from_path(path)
        for i in range(len(images)):
            now = datetime.now().strftime('%m-%d-%Y-%H-%M-%S')
            images[i].save(f'{path_to_save}{os.path.sep}{filename}-page{i + 1}-{now}.png', 'PNG')
    except:
        result = 'No PDF found!'
        messagebox.showinfo('Result', result)
    else:
        result = 'Success!'
        messagebox.showinfo('Result', result)


master = Tk()
Label(master, text="File Location").grid(row=0, sticky=W)

entry = Entry(master)
entry.grid(row=0, column=1)

button = Button(master, text="Convert", command=pdf2img)
button.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()
