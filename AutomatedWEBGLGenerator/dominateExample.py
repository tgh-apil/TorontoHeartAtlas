# import dominate
# from dominate.tags import *

# doc = dominate.document(title='Dominate your HTML')

# with doc.head:
#     link(rel='stylesheet', href='style.css')
#     script(type='text/javascript', src='script.js')

# with doc:
#     with div(id='header').add(ol()):
#         for i in ['home', 'about', 'contact']:
#             li(a(i.title(), href='/%s.html' % i))

#     with div():
#         attr(cls='body')
#         p('Lorem ipsum..')

# print(doc)

import dominate
from dominate.tags import *

table_headers = ['Column 1', 'Another One', 'Ehmmmm']

def create_page():
    doc = dominate.document(title='Example Table')

    with doc.head:
        link(rel='stylesheet', href='style.css')

    with doc:
        with div(cls='container'):
            h1('Hello, World!')
            with table(id='main', cls='table table-striped'):
                caption(h3('A table to show data'))
                with thead():
                    with tr():
                        for table_head in table_headers:
                            th(table_head)
                with tbody():
                    for i in range(10):
                        with tr():
                            td('Hello')
                            td('Another one')
create_page()