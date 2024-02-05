from PIL import Image
from asso import associations
import os


class Symbol:

    symbols = {}

    def insert(self, character, image):
        self.symbols[character] = image

    def find(self, character):
        return self.symbols[character]

    def InitializeImages(self, path):
        files = os.listdir(path)
        for i in files:
            symbol_name = i
            symbol_path = "Symbols/"+symbol_name
            image = Image.open(symbol_path)
            character = associations[symbol_name]
            self.insert(character, image)
