def double(valor, currency=False):
    valor *= 2
    if currency:
        return coin(valor)
    else:
        return valor


def triple(valor, currency=False):
    valor *= 3
    if currency:
        return coin(valor)
    return valor


def discount(valor, porcentagem, currency=False):
    valor += porcentagem * (valor/100)
    if currency:
        return coin(valor)
    return valor


def fees(valor, porcentagem, currency=False):
    valor -= porcentagem * (valor/100)
    if currency:
        return coin(valor)
    return valor


def coin(value, currency='R$'):
    value = f'{value:.2f}'
    return f'{currency}{value.replace(".", ",")}'


def summary(value, disc, fee, currency=False):
    print('-='*20)
    print(f'\033[33mDobro do valor\033[m: {double(value, currency)}')
    print(f'\033[33mTriplo do valor\033[m: {triple(value, currency)}')
    print(f'\033[33mValor com {disc}% de desconto\033[m: {discount(value, disc, currency)}')
    print(f'\033[33mValor com {fee}% de juros\033[m: {fees(value, fee, currency)}')
    print('-='*20)
