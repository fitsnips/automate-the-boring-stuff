#! python3

def spam():
    bacon()

def bacon():
    raise Exception('This is the Error message')

spam()