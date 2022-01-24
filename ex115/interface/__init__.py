def options(list_, color=8):
    for count, i in enumerate(list_):
        print(f'\033[3{color}m[{count+1}]\033[m {i}')


def title(text, color1=8, color2=8):
    print(f'\033[3{color1}m{"-="}\033[m'*20)
    print(f'\033[1;3{color2}m{text.center(40)}\033[m')
    print(f'\033[3{color1}m{"-="}\033[m'*20)
