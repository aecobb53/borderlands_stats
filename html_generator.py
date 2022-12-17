import json
from phtml.document import Document
from phtml.classes import (
    Header,
    Link,
    HyperLink,
    Title,
)


class CharacterHTML:
    def __init__(self):
        self.body = []
        self.doc = Document()

    def return_html(self, characters=[]):

        """Header"""
        h_link = HyperLink(href='favicon.ico', rel='shortcut icon', type='image/x-icon')
        self.doc.head.append(Title(content='Borderlands Classes'))
        self.doc.head.append(
            h_link
        )




        self.doc.body.append(Header(1, 'Borderlands 3 Characters'))
        h2 = Header(2, 'Borderlands 3 Characters')
        h2.add_class('this')
        a = self.doc.return_document
        h2.add_style({'text-align': 'center'})
        self.doc.body.append(h2)
        b = self.doc.return_document
        return self.doc.return_document

        details = [
            '<!DOCTYPE html>',
            '<html>',
        ]

        # details.append('<head>')
        # details.append(f'<title>Borderlands Classes</title>')
        # self.doc.head.append()



        # details.append(f'<link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />')




        # details.append('</head>')
        """Body"""
        # details.append('<body>')
        
        """
        This function needs to be updated to phtml
        """
        for c in characters:
            if not c.active:
                continue
            self.body.append(c.generate_html_tile())
        a = [l for l in self.body]
        details.extend([l for l in self.body])
        details.append(self.return_css())
        # details.append('</body>')
        # details.append('</html>')
        # details.append(f'<img src="html_images/Emblem_on_white_background.png">')
        return '\n'.join(details)

    def save_html(self, filepath='class_builds.html', characters=[]):
        with open(filepath, 'w') as hf:
            hf.write(self.return_html(characters))

    def return_css(self):
        styles = []
        with open('html_style/tiles.css', 'r') as cf:
            for line in cf.readlines():
                styles.append(line.strip())
        return f"<style>{''.join(styles)}</style>"

# c= CharacterHTML()
# deets = c.return_html()

# x=1

# class CharacterHTML:
#     def __init__(self):
#         self.body = []

#     def return_html(self, characters=[]):
#         self.body.append('<h1>Borderlands 3 Characters</h1>')
#         self.body.append('<h2 style="text-align:center;">Characters</h2>')
#         for c in characters:
#             if not c.active:
#                 continue
#             self.body.append(c.generate_html_tile())
#         details = [
#             '<!DOCTYPE html>',
#             '<html>',
#         ]

#         """Header"""
#         details.append('<head>')
#         details.append(f'<title>Borderlands Classes</title>')
#         details.append(f'<link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />')
#         details.append('<link rel="icon" type="image/x-icon" href="/images/favicon.ico">')
#         details.append('</head>')
#         """Body"""
#         details.append('<body>')
#         details.extend([l for l in self.body])
#         details.append(self.return_css())
#         details.append('</body>')
#         details.append('</html>')
#         # details.append(f'<img src="html_images/Emblem_on_white_background.png">')
#         return '\n'.join(details)

#     def save_html(self, filepath='class_builds.html', characters=[]):
#         with open(filepath, 'w') as hf:
#             hf.write(self.return_html(characters))

#     def return_css(self):
#         styles = []
#         with open('html_style/tiles.css', 'r') as cf:
#             for line in cf.readlines():
#                 styles.append(line.strip())
#         return f"<style>{''.join(styles)}</style>"
