from PIL import Image
from src.Symbols import Symbol
from src.Svg import Svg
import tkinter as tk
from tkinter import filedialog
import os
import shutil


path = './Symbols'

WIDTH = 180.0
HEIGHT = 60.0


def CreateFinalImage(word):
    word_length = len(word)
    image_final = Image.new('RGBA', (0, 0), (0, 0, 0, 0))
    width = image_final.width
    height = image_final.height

    value = 20

    for i in range(word_length):
        image_symbol = Symbol.find(word[i])

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
    label_image.place(x=10, y=60)


def Convert():
    word = text_area.get().lower()
    image = CreateFinalImage(word)
    if not os.path.exists('temp'):
        os.makedirs('temp')
    image.save('temp/temp.png')
    ShowImage()


def SaveImagePNG():
    file_directory = filedialog.asksaveasfilename(defaultextension='.png')
    shutil.copy('temp/temp.png', file_directory)


def SaveImageSVG():
    word = text_area.get().lower()
    file_directory = tk.filedialog.asksaveasfilename(defaultextension='.svg')
    svg_image = Svg.convert_text_to_svg(word)
    with open(file_directory, "w") as file:
        file.write(svg_image)



Symbol.InitializeImages(path)

window = tk.Tk()
window.title('BrailleMaker')
window.geometry("640x180")
image_created = False

label = tk.Label(window, text='Palavra a ser transformada:')
text_area = tk.Entry(window)
button_convert = tk.Button(window, text='Converter', command=Convert)
button_save_png = tk.Button(window, text='Salvar PNG', command=SaveImagePNG)
button_save_svg = tk.Button(window, text='Salvar SVG', command=SaveImageSVG)

label.grid(column=0, row=0)
label.place(x=10, y=9)
text_area.grid(column=1, row=0)
text_area.place(x=160, y=9)
button_convert.grid(column=2, row=0)
button_convert.place(x=300, y=5)
button_save_png.grid(column=0, row=2)
button_save_png.place(x=10, y=140)
button_save_svg.grid(column=0, row=2)
button_save_svg.place(x=95, y=140)

window.mainloop()

if os.path.exists("temp"):
    if os.path.exists("temp/temp.png"):
        os.remove("temp/temp.png")
    os.rmdir("temp")
