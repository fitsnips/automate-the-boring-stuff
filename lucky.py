#! python3
# lucky.py - Opens serveral google search results.

import requests, sys, webbrowser, bs4, logging

# log format
logging.basicConfig(filename='logging/lucky.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


print('Googleing...') # display text while pulling down google search page
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
try:
    res.raise_for_status()
except:
    print('There was a problem: %s' % (exc))

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')



# Opens a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
