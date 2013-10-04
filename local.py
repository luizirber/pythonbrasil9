from IPython.nbconvert.exporters import SlidesExporter
from IPython.config import Config

from IPython.nbformat import current as nbformat


# This is the config object I talked before:
# After the 'url_prefix', you can set the location of your
# local reveal.js library, i.e. if the reveal.js is located
# in the same directory as your talk.slides.html, then
# set 'url_prefix':'reveal.js'.

c = Config({
    'RevealHelpTransformer': {
        'enabled': True,
        'url_prefix': 'reveal.js',
    },
})

exportHtml = SlidesExporter(config=c)

for talk in ("numba", "rosalind"):
    infile = "%s.ipynb" % talk  # load the name of your slideshow
    outfile = "%s.slides.html" % talk

    with open(infile) as f:
        notebook = f.read()
        notebook_json = nbformat.reads_json(notebook)

    (body, resources) = exportHtml.from_notebook_node(notebook_json)

    with open(outfile, 'w') as out:
        out.write(body.encode('utf-8'))
