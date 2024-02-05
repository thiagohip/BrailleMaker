class Svg:
    header = ('<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN" '
              '"http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">\n<svg width="600px" height="700px" '
              'xmlns="http://www.w3.org/2000/svg">\n<desc>SVG Output</desc>\n')

    footer = "\n</svg>"

    characters = {"a": [[1, 0], [0, 0], [0, 0]],
                  "b": [[1, 0], [1, 0], [0, 0]],
                  "c": [[1, 1], [0, 0], [0, 0]],
                  "d": [[1, 1], [0, 1], [0, 0]],
                  "e": [[1, 0], [0, 1], [0, 0]],
                  "f": [[1, 1], [1, 0], [0, 0]],
                  "g": [[1, 1], [1, 1], [0, 0]],
                  "h": [[1, 0], [1, 1], [0, 0]],
                  "i": [[0, 1], [1, 0], [0, 0]],
                  "j": [[0, 1], [1, 1], [0, 0]],
                  "k": [[1, 0], [0, 0], [1, 0]],
                  "l": [[1, 0], [1, 0], [1, 0]],
                  "m": [[1, 1], [0, 0], [1, 0]],
                  "n": [[1, 1], [0, 1], [1, 0]],
                  "o": [[1, 0], [0, 1], [1, 0]],
                  "p": [[1, 1], [1, 0], [1, 0]],
                  "q": [[1, 1], [1, 1], [1, 0]],
                  "r": [[1, 0], [1, 1], [1, 0]],
                  "s": [[0, 1], [1, 0], [1, 0]],
                  "t": [[0, 1], [1, 1], [1, 0]],
                  "u": [[1, 0], [0, 0], [1, 1]],
                  "v": [[1, 0], [1, 0], [1, 1]],
                  "w": [[0, 1], [1, 1], [0, 1]],
                  "x": [[1, 1], [0, 0], [1, 1]],
                  "y": [[1, 1], [0, 1], [1, 1]],
                  "z": [[1, 0], [0, 1], [1, 1]],
                  "á": [[1, 0], [1, 1], [1, 1]],
                  "à": [[1, 1], [1, 0], [0, 1]],
                  "é": [[1, 1], [1, 1], [1, 1]],
                  "!": [[0, 0], [1, 1], [1, 0]],
                  "ç": [[1, 1], [1, 0], [1, 1]],
                  "í": [[0, 1], [0, 0], [1, 0]],
                  "ó": [[0, 1], [0, 0], [1, 1]],
                  "ú": [[0, 1], [1, 1], [1, 1]],
                  ".": [[0, 0], [1, 1], [0, 1]]
                  }

    def convert_char_to_svg(self, char, cx):
        char_svg = ""

        j = self.characters[char]

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

    def convert_text_to_svg(self, text):
        text_svg = self.header
        cx = 10
        for i in text:
            if not i == ' ':
                text_svg += self.convert_char_to_svg(i, cx)

            cx += 30

        text_svg += self.footer

        return text_svg