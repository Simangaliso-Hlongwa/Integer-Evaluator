x = int(input('Enter integer: '))
if x%2 == 0:
    print('even')
else:
    print('odd')
    if x%3 != 0:
        print('and not didvisble by three')
    if x%3 == 0:
        print('is divisible by three')
