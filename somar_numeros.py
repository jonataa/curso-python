'''
Faça um programa que leia um arquivo,
com um número em cada linha, e imprima
a soma destes números.
'''
f = open('numeros.txt', 'r')
soma = 0
for line in f:
    soma += int(line)
f.close()

fw = open('soma.txt', 'w')
fw.write(str(soma))
fw.close()
