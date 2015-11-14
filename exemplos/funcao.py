# Faça um programa que peça um número e diga se ele é bonito.
# Um número bonito possui o digito 4 e não possui o digito 9.
def numerobonito(numero):
    if "4" in numero and "9" not in numero:
        print ("Número bonito")
    else:
        print ("Número feio")

n = input("Digite um número: ")
numerobonito(n)
        


