'''
Faça um programa que peça uma palavra e
verifique se ela é palíndromo.
'''
texto = input('Palavra: ').lower()
if texto == texto[::-1]:
    print ('É palíndromo.')
else:
    print ('Não é palíndromo.')
