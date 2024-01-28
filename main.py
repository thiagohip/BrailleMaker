from PIL import Image
import src.Symbols as Symbols
import tkinter as tk
from tkinter import filedialog
import os
import shutil


json_file = open('asso.json')
path = './Symbols'


def CreateFinalImage(word):

    word_length = len(word)
    image_final = Image.new('RGBA', (0, 0), (0, 0, 0, 0))
    width = image_final.width
    height = image_final.height

    value = 20

    for i in range(word_length):
        image_symbol = Symbols.find(word[i]).image

        image_temp = Image.new('RGBA', (width + image_symbol.width, max(height, image_symbol.height)), (0, 0, 0, 0))
        image_temp.paste(image_final, (0, 0))
        image_temp.paste(image_symbol, (width, 0))
        width = width + image_symbol.width + value
        height = max(height, image_symbol.height)
        image_final = image_temp

    return image_final


def ShowImage():
    global img_final
    img_final = tk.PhotoImage(file="temp/temp.png")
    label_image = tk.Label(window, image=img_final)
    label_image.grid(column=0, row=1)


def Convert():
    word = text_area.get()
    image = CreateFinalImage(word)
    if not os.path.exists('temp'):
        os.makedirs('temp')
    image.save('temp/temp.png')
    ShowImage()


def SaveImage():
    file_directory = filedialog.asksaveasfilename(defaultextension='.png')
    shutil.copy('temp/temp.png', file_directory)


Symbols.InitializeImages(path, json_file)

window = tk.Tk()
window.title('BrailleMaker')
window.resizable(False, False)
image_created = False

label = tk.Label(window, text='Palavra a ser transformada')
text_area = tk.Entry(window)
button_convert = tk.Button(window, text='Converter', command=Convert)
button_save = tk.Button(window, text='Salvar', command=SaveImage)

label.grid(column=0, row=0)
text_area.grid(column=1, row=0)
button_convert.grid(column=2, row=0)
button_save.grid(column=0, row=2)

window.mainloop()
if os.path.exists("temp/temp.png"):
    os.remove("temp/temp.png")
