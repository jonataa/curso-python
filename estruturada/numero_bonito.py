'''
Um número bonito possui
o digito 4 e não possui o digito 9.
Faça um programa que peça um número e diga se
ele é bonito.
'''
n = input('Número: ')

if '4' in n and '9' not in n:
    print ('%s é um número bonito!' %n)
else:
    print ('%s é um número feio!' %n)
