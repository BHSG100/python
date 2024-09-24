import random

palavras = ["arthur", "carlos", "celso", "ze raimundo", "vanessao", "sheldon"]
palavraEscolhida = random.choice(palavras)
print("A Palavra sorteada tem " + str(len(palavraEscolhida)) + " Letras.")



erro = len(palavraEscolhida) - 1
erros = 0

while erros < erro:
    l = input("Informe uma letra: ")
    for letra in palavraEscolhida:
        if l == letra:
            print("A letra " + str(l) + " está na posição " + str(palavraEscolhida.index(l) + 1))
    else:
        erros += 1