'''
Data com mês por extenso. Construa uma função que receba
uma data no formato DD/MM/AAAA e devolva uma string
no formato D de mesPorExtenso de AAAA.
Ex: 13/09/1987 -> 13 de setembro de 1987
'''
d = input('Data (dd/mm/yyyy): ')
dia, mes, ano = d.split('/')
meses = ['janeiro', 'fevereiro', 'março',
         'abril', 'maio', 'junho', 'julho',
         'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro']
mes = int(mes) - 1
print ('%s de %s de %s' %(dia, meses[mes], ano)) 
