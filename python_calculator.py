operation = ''

def addition(st_arg: float, nd_arg: float) -> float:
    return st_arg + nd_arg

def subtraction(st_arg: float, nd_arg: float) -> float:
    return st_arg - nd_arg

def multiplication(st_arg: float, nd_arg: float) -> float:
    return st_arg * nd_arg

def division(st_arg: float, nd_arg: float) -> float:
    return st_arg / nd_arg

def percentage(st_arg: float, nd_arg: float) -> float:
    res_one = division(st_arg, 100)
    res_two = multiplication(res_one, nd_arg)
    return res_two

def proportion(st_arg: float, nd_arg: float, rd_arg: float) -> float:
    res_one = multiplication(rd_arg, nd_arg)
    res_two = division(res_one, st_arg)
    return res_two

while operation != 0:
    print('Choose your math operation:\n'
          '1 - Addiction;\n'
          '2 - Subtraction;\n'
          '3 - Multiplication;\n'
          '4 - Division;\n'
          '5 - Percentage;\n'
          '6 - Proportion;\n'
          '0 - Exit.')
    operation = int(input('Select an option: '))

    match operation:
        case 1:  # Addition
            st_num = float(input('\nFirst number: '))
            nd_num = float(input('Second number: '))
            result = addition(st_num, nd_num)
            print('Result of {} + {} is {}.\n'.format(st_num, nd_num, result))

        case 2:  # Subtraction
            st_num = float(input('\nFirst number: '))
            nd_num = float(input('Second number: '))
            result = subtraction(st_num, nd_num)
            print('Result of {} - {} is {}.\n'.format(st_num, nd_num, result))

        case 3:  # Multiplication
            st_num = float(input('\nFirst number: '))
            nd_num = float(input('Second number: '))
            result = multiplication(st_num, nd_num)
            print('Result of {} * {} is {}.\n'.format(st_num, nd_num, result))

        case 4:  # Division
            st_num = float(input('\nFirst number: '))
            nd_num = float(input('Second number: '))
            result = division(st_num, nd_num)
            print('Result of {} / {} is {}.\n'.format(st_num, nd_num, result))

        case 5:  # Percentage
            print('\n"%" of "n".')
            st_num = float(input('First number (%): '))
            nd_num = float(input('Second number (n): '))
            result = percentage(st_num, nd_num)
            print('Result of {}% of {} is {}.\n'.format(st_num, nd_num, result))

        case 6:  # Proportion
            print('\nIf "x" is equivalent to "%", "y" equals ?')
            st_num = float(input('First number (x): '))
            nd_num = float(input('Second number (%): '))
            rd_num = float(input('Third number (y): '))
            result = (rd_num * nd_num) / st_num
            print('If {} is equivalent to {}%, {} is equivalent to {}.\n'.format(st_num, nd_num, rd_num, result))

        case 0:
            print('\nBye bye, see you soon!')

        case _:
            print('\n***\n*** PLEASE CHOOSE A VALID NUMBER.\n***\n')
