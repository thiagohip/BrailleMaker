import json

class Svg:
    header = ('<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN" '
              '"http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">\n<svg width="600px" height="700px" '
              'xmlns="http://www.w3.org/2000/svg">\n<desc>SVG Output</desc>\n')

    footer = "\n</svg>"

    with open("./char.json") as file:
        characters = json.load(file)

    @classmethod
    def convert_char_to_svg(cls, char, cx):
        char_svg = ""

        j = cls.characters[char]

        if j[0][0] == 1:
            char_svg += f'<circle cx="{cx}" cy="10" r="3" stroke-width="1" stroke="#000000" fill="#000000" fill-opacity="1"/>\n'
        else:
            char_svg += f'<circle cx="{cx}" cy="10" r="1" stroke-width="1" stroke="none" fill="#000000" fill-opacity="1"/>\n'

        cx += 10

        if j[0][1] == 1:
            char_svg += f'<circle cx="{cx}" cy="10" r="3" stroke-width="1" stroke="#000000" fill="#000000" fill-opacity="1"/>\n'
        else:
            char_svg += f'<circle cx="{cx}" cy="10" r="1" stroke-width="1" stroke="none" fill="#000000" fill-opacity="1"/>\n'

        cx -= 10

        if j[1][0] == 1:
            char_svg += f'<circle cx="{cx}" cy="20" r="3" stroke-width="1" stroke="#000000" fill="#000000" fill-opacity="1"/>\n'
        else:
            char_svg += f'<circle cx="{cx}" cy="20" r="1" stroke-width="1" stroke="none" fill="#000000" fill-opacity="1"/>\n'

        cx += 10

        if j[1][1] == 1:
            char_svg += f'<circle cx="{cx}" cy="20" r="3" stroke-width="1" stroke="#000000" fill="#000000" fill-opacity="1"/>\n'
        else:
            char_svg += f'<circle cx="{cx}" cy="20" r="1" stroke-width="1" stroke="none" fill="#000000" fill-opacity="1"/>\n'

        cx -= 10

        if j[2][0] == 1:
            char_svg += f'<circle cx="{cx}" cy="30" r="3" stroke-width="1" stroke="#000000" fill="#000000" fill-opacity="1"/>\n'
        else:
            char_svg += f'<circle cx="{cx}" cy="30" r="1" stroke-width="1" stroke="none" fill="#000000" fill-opacity="1"/>\n'

        cx += 10

        if j[2][1] == 1:
            char_svg += f'<circle cx="{cx}" cy="30" r="3" stroke-width="1" stroke="#000000" fill="#000000" fill-opacity="1"/>\n'
        else:
            char_svg += f'<circle cx="{cx}" cy="30" r="1" stroke-width="1" stroke="none" fill="#000000" fill-opacity="1"/>\n'

        return char_svg

    @classmethod
    def convert_text_to_svg(cls, text):
        text_svg = cls.header
        cx = 10
        for i in text:
            if not i == ' ':
                text_svg += cls.convert_char_to_svg(i, cx)

            cx += 30

        text_svg += cls.footer

        return text_svg