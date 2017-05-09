
while True:
    try:
        number = int(input('What is your favorite number?\n'))
        print(2/number)
        break
    except ValueError:
        print('Make sure and enter a number.')
    except ZeroDivisionError:
        print('Any other number appart from 0 (zero)')