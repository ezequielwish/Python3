# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com')
except:
    print('This website is not working.')
else:
    print('This website is working!')
