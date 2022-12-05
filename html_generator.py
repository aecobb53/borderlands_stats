import json


class CharacterHTML:
    def __init__(self):
        self.body = []

    def return_html(self, characters=[]):
        self.body.append('<h1>Borderlands 3 Characters</h1>')
        self.body.append('<h2 style="text-align:center;">Characters</h2>')
        for c in characters:
            if not c.active:
                continue
            self.body.append(c.generate_html_tile())
        details = [
            '<!DOCTYPE html>',
            '<html>',
            '<body>',
        ]
        details.extend([l for l in self.body])
        details.append(self.return_css())
        details.extend([
            '</body>',
            '</html>',
        ])
        return ''.join(details)

    def save_html(self, filepath='details.html', characters=[]):
        with open(filepath, 'w') as hf:
            hf.write(self.return_html(characters))

    def return_css(self):
        styles = []
        with open('html_style/tiles.css', 'r') as cf:
            for line in cf.readlines():
                styles.append(line.strip())
        return f"<style>{''.join(styles)}</style>"
