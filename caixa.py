saque = int(input("qual o valor do saque: "))
resto = 0

duzentos = saque//200
saque %= 200
resto %= 200

cem = saque//100
saque %= 100
resto %= 100

cinquenta = saque//50
saque %= 50
resto %= 50

vinte = saque//20
saque %= 20
resto %= 20

dez = saque//10
saque %= 10
resto %= 10

cinco = saque//5
saque %= 5
resto %= 5

resto %= 1

if duzentos > 0:
    print(str(duzentos) + " nota(s) de duzentos")
if cem > 0:
    print(str(cem) + " nota(s) de cem")
if cinquenta > 0:
    print(str(cinquenta) + " nota(s) de cinquenta")
if vinte > 0:
    print(str(vinte) + " nota(s) de vinte")
if dez > 0:
    print(str(dez) + " nota(s) de dez")
if cinco > 0:
    print(str(cinco) + " nota(s) de cinco")
if resto > 0:
    print(resto)