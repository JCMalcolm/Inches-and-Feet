def inches_to_feet():
    try:
        user_input = input('Enter inches to convert: ')
        inches = int(user_input)
        print(f'{inches} inches is equal to {inches//12} feet and {inches%12} inches.')
    except:
        print('Please use whole numbers. Round to nearest whole number if need be. \n\t Please try again.')
        inches_to_feet()

def feet_to_inches():

    try:
        x = input('Enter feet to convert: ')
        y = input('Enter additional inches: ')
        feet = int(x)
        inches = int(y)
        print(f'{feet} feet and {inches} inches is equal to {feet*12+inches} inches.')
    except:
        print('Please use whole numbers. Round to nearest whole number if need be. \n\t Please try again.')
        feet_to_inches()
