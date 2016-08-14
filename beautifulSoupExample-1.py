#! python3

import requests, bs4

res = requests.get('http://nostarch.com')

# check for errors, this one should be fine
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc) )

noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))

