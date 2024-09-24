for x in range(5):
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