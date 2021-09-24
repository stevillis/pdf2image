import os
from datetime import datetime
from tkinter import *
from tkinter import messagebox

from pdf2image import convert_from_path

HELP_TEXT = "Se o caminho 'Salvar em' não for informado, \nas imagens serão salvas no mesmo diretório do arquivo PDF"


def pdf2img():
    try:
        path_file_location = str(entry_file_location.get())
        path_to_save, filename = os.path.split(path_file_location)

        path_file_destination = str(entry_file_destination.get())
        if len(path_file_destination) > 0:
            path_to_save = path_file_destination

        images = convert_from_path(path_file_location)
        for i in range(len(images)):
            now = datetime.now().strftime('%m-%d-%Y-%H-%M-%S')
            images[i].save(f'{path_to_save}{os.path.sep}{filename}-page{i + 1}-{now}.png', 'PNG')
    except:
        result = 'Nenhum PDF encontrado!'
        messagebox.showinfo('Resultado', result)
    else:
        result = 'Imagens salvas com sucesso!'
        messagebox.showinfo('Resultado', result)


master = Tk()
master.title('Conversor de PDF para Imagem')
Label(master, text="Caminho do PDF:").grid(row=0, sticky=W)
Label(master, text="Salvar em:").grid(row=1, sticky=W)
Label(master, text=HELP_TEXT).grid(row=2, columnspan=2)

entry_file_location = Entry(master, width=40)
entry_file_location.grid(row=0, column=1)

entry_file_destination = Entry(master, width=40)
entry_file_destination.grid(row=1, column=1)

button = Button(master, text="Converter", command=pdf2img)
button.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()
