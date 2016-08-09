#! python3

def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater then two!')
    if height <= 2:
        raise Exception('Height must be greater then two!')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width -2) + symbol ))
    print(symbol * width)

for sym, w, h in (('*', 1, 4), ('O', 20, 5), ('x', 1, 3), ('Z', 3, 3)):
    try:
        boxPrint(sym,w,h)
    except Exception as err:
        print('An error has occured: ' + str(err))
