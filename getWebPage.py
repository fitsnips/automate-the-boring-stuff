#! python3

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# check for errors, this one should be fine
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc) )
len(res.text)

print(res.text[:250])

res = requests.get('https://automatetheboringstuff.com/files/page_that_does_not_exist.txt')

# check for errors, this should raise a error
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc) )