##criar uma função
def imprimir(texto=""):
     print(texto)

def media():
    aluno = input("Informre o nome do aluno: ")
    N1 = int(input("Informe a nota 1 do aluno: "))
    N2 = int(input("Informe a nota 2 do aluno: "))
    N3 = int(input("Informe a nota 3 do aluno: "))
    Media = (N1+N2+N3)/3
    if Media >= 6:
        print(aluno + " está de parabéns!!!")
    if Media == 5:
        print(aluno + "da para melhorar")
    if Media <= 4:
        print(aluno + " estude mais")
    print(Media)

def CalculadoraIMC(peso, altura):
    imc = peso/(altura*altura)
    imprimir(imc)
    if imc < 18.8:
        imprimir("voçê esta abaixo do peso")
    elif 18.5 < imc < 24.99:
        imprimir("Voçê esta com o peso normal")
    elif imc > 25 and imc < 29.99:
        imprimir("Voçê esta sobrepeso")
    else:
        imprimir("voçê esta com obesidade")

peso = float(input("qual seu peso ?"))
altura = float(input("qual a sua altura"))

CalculadoraIMC(peso, altura)

def dias_vividos():
    ano_atual = 2024
    quantos_dias = (ano_atual - ano_de_nascimento) * 365
    horas_vividas = quantos_dias * 24
    minutos_vividos = horas_vividas * 60
    segundos_vividos = minutos_vividos * 60
    imprimir(quantos_dias)
    imprimir(horas_vividas)
    imprimir(minutos_vividos)
    imprimir(segundos_vividos)

ano_de_nascimento = int(input("que ano voçê nasceu? "))
dias_vividos()