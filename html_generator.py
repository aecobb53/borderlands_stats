import json


class CharacterHTML:
    def __init__(self):
        self.body = []

    def return_html(self, characters=[]):
        self.body.append('<h1>Borderlands 3 Characters</h1>')
        self.body.append('<h2>Tiles</h2>')
        for c in characters:
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
        css = [
            '<style>',
            'body {background-color: #282828;}',
            'h1   {color: #f4f4f4;}',
            'p    {color: red;}',
            '.tiles {margin:50px; padding:10px; display: border-style: solid; border-color: purple;}',
            # '.tile {margin:10px; padding:10px; display: inline-block; border-style: solid;}',
            '.tile {margin:10px; padding:10px; display: inline-block; border-style: solid; border-color: coral; background-color: #373737;}',
            '</style>',
        ]
        return ''.join(css)