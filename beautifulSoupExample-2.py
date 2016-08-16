#! python3

# extract the author from a html file using css tags

import bs4

exampleFile = open('examples/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
authorName = elems[0].getText()
print(authorName)
print(str(elems[0]))
print(elems[0].attrs)
