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

# save to a file but must be 'wb' write binary to save
# unicode
playFile = open('./examples/RomeoAndJuliet.txt', 'wb')

# we write in chunks to control memory usage
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

res = requests.get('https://automatetheboringstuff.com/files/page_that_does_not_exist.txt')

# check for errors, this should raise a error
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc) )