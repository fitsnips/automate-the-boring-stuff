#! python3

import random, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# initialize empty guess
guess = ''

# make sure they enter either heads or tails, if not ask again.
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0,1) # 0 is tails, 1 is heads
logging.debug('Toss is %s: ' % toss)

# this feels wrong but it works ...
if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'

# now lets see if they guessed correctly, if not give them a second try on the same flip
if toss == guess:
    print('You got it')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game!')