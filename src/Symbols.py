from PIL import Image
import os
import json

class Symbol:

    symbols = {}

    @classmethod
    def insert(cls, character, image):
        cls.symbols[character] = image

    @classmethod
    def find(cls, character):
        return cls.symbols[character]

    @classmethod
    def InitializeImages(cls, path):
        with open("./asso.json") as file:
            associations = json.load(file)

        files = os.listdir(path)
        for i in files:
            symbol_name = i
            symbol_path = "Symbols/"+symbol_name
            image = Image.open(symbol_path)
            character = associations[symbol_name]
            cls.insert(character, image)
