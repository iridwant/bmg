n = 50

for i in range(1, n+1):
    if i % 5 == 0 and i % 3 == 0:
        print('Frontend Backend', end=',')
    elif i % 5 == 0:
        print('Backend', end=',')
    elif i % 3 == 0:
        print('Frontend', end=',')
    else:
        print(i, end=',')