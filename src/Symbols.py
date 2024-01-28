from PIL import Image
import json
import os


symbols = []


class Symbol:

    def __init__(self, character, image):
        self.character = character
        self.image = image


def insert(character, image):
    symbol = Symbol(character, image)
    symbols.append(symbol)


def find(character):
    for i in symbols:
        if i.character == character:
            return i


def InitializeImages(path, json_file):
    files = os.listdir(path)
    names = json.load(json_file)
    for i in files:
        symbol_name = i
        symbol_path = "Symbols/"+symbol_name
        image = Image.open(symbol_path)
        character = names[symbol_name]
        insert(character, image)