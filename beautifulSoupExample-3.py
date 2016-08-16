#! python3

import requests, bs4, webbrowser, logging

# log format
logging.basicConfig(filename='logging/ebay-logfile.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



# search ebay for "safe"
res = requests.get('https://www.ebay.com/sch/i.html?_nkw=safe')

try:
    res.raise_for_status()
except:
    print('There was a problem: %s' % (exc) )

# return is unicode so convert to text for html.parser
exampleSoup = bs4.BeautifulSoup(res.text, "html.parser")

# pull the links from the page, using ListView class=lvtitle
links = exampleSoup.select('.lvtitle a')

# how man items did we get on this search, 50 per a page
# select must be bad as we are returning more then 50
# and default items per a page is 50
# TODO: clean up select
logging.debug('Number of #links: %s' % (str(len(links))) )

if len(links) > 50:
    print('At least fifty items found')
    logging.debug('Content of #links: %s' % (str(links)))
else:
    print('Number if items found %s ' % len(links))

# open up a webbrowser with the first search result
webbrowser.open(links[0].get('href'))

logging.shutdown()
