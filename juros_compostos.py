juros = int(input("qual a porcentagen: "))/100
valor = int(input("quanto você quer investir: "))
tempos = int(input("quanto tempo(em meses): "))
montante = valor*((1+juros)**(tempos))
print (montante)