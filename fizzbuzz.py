#! python3

for i in range(1,100):
    div3 = False
    div5 = False

    # print(i)
    if i % 3 == 0:
        div3 = True
    if i % 5 == 0:
        div5 = True

    if div3 and div5:
       print('fizzbuzz')
    elif div3:
       print('fizz')
    elif div5:
       print('buzz')
    else:
       print(i)