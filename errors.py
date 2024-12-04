def convert_to_integer(value):
    try:
        result = int(value)
        print(f'Conversion succesful! Result: {result}')
    except:
        print('Conversion failed. Plase enter a valid integer')
    else: # only happens if no exceptions occured
        print('Else invoked')
    finally: # Happens no matter what
        print('Closing any open resources')

# User input
spam = input('Enter a number to conver to integer: ')
convert_to_integer(spam)