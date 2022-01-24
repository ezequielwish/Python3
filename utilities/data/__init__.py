def moneyput(text):
    valid = False
    while not valid:
        input_ = input(text).replace(',', '.').strip()
        if input_.isalpha() or input_ == '':
            print('\033[31mERROR! Value not monetary.\033[m')
        else:
            valid = True
            return float(input_)


def floatput(text):
    """
    Works like Input function, but only accept Float numbers
    :param text: the input text
    :return: the typed Float or Int number as float.
    """
    while True:
        try:
            number = float(input(text))
        except (ValueError, TypeError):
            print('\033[31mERROR! Value not float.\033[m')
        else:
            return number


def intput(text):
    """
    Works like Input function, but only accept Int numbers
    :param text: the input text
    :return: the typed Int number
    """
    while True:
        try:
            number = int(input(text))
        except (ValueError, TypeError):
            print('\033[31mERROR! Value not int.\033[m')
        else:
            return number


def flagput(text, flag):
    """
    Only accept input of a predetermined Flag
    :param text: the input text
    :param flag: flag as string without spaces. Ex: 'YN'
    :return: Typed value
    """
    while True:
        answer = str(input(text)).strip().upper()[0]
        if answer in flag.upper():
            break
        else:
            print('\033[31mERROR! Try again.\033[m')
    return
