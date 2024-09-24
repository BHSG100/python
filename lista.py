#import random

#nomes = ["Raul", "Gabi", "Arthur", "Bruno", "Guilheme"]

#times = ["Ibis", "Paysandu", "Ponte Preta", "Barcelona", "Real Madri"]

#time = times[random.randrange(0,4)]

#print(nomes[random.randrange(0,4)] +" torce para o " + time)

#print(time + " is the best! SQN")

#notas = [5,9,8,4,5,5]

#print(len(nomes))
#print(len(nomes))
#print(len(times))

#nomes.sort()
#nomes.sort()
#nomes.reverse()

#print(nomes)
#print(max(nomes))
#print(min(nomes))

nomes = []

for x in range(26):
    nome = input("informe um nome :")
    nomes.append(nome)
nomes.sort()

print(nomes)
