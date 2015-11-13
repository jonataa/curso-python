# Calcule a média de 5 notas
i = 1
notas = []
while i <= 5:
    nota = float(input('Nota %d: ' %i))
    notas.append(nota)
    i += 1
média = sum(notas) / len(notas)
print ('Média = %.1f' %média)
