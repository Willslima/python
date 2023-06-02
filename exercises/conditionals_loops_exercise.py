number = int(input('Type a number'))

if number %3 != 0 and number %5 != 0:
    print('this number nots a mutiple of 3 or 5')
if number %3 == 0 and number %5 == 0:
    print('this number is mutiple of 3 and 5')
elif number % 3 == 0:
    print('this number is mutiple of 3')
elif number % 5 == 0:
    print('this number is mutiple of 5')