h=float(input("Digite sua altura: "))
sx=input("Digite seu Sexo (M ou H) ").lower()
if(sx == "h"):
    print("O seu peso ideal é: ", h + 72.7*h - 58)
else:
    print("O seu peso ideal é: ", h + 62.1*h - 44.7)