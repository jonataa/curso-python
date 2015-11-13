s = float(input('Salário em R$: '))
p = int(input('Aumento em %: '))
aumento = (p / 100) * s
print ('Novo salário = R$ %.2f' %(s + aumento))
