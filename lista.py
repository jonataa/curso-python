# Exercício - Leia 5 números inteiros e salve numa lista.
# Imprima a lista para o usuário.
# https://github.com/jonataa/curso-python
lista = []
i = 1
while i <= 5:
    n = int(input('Digite o número %d: ' %i))
    lista.append(n)
    i = i + 1
print (lista)
