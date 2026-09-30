nota = 0
while True:
    nota=float(input("digite uma nota de 0 a 10: "))

    if(nota < 0 or nota > 10):
        input("VALOR IVALIDO! digite novamente uma nota entre 0 a 10: ")
    else:
        break

print("nota válida:",nota)
