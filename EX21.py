a=float(input("Digite o coeficiente A: "))

if(a == 0):
    print("Devido ao coeficiente A ser igual a Zero, não é uma equação de segundo grau.")
else:
    b=float(input("Digite o coeficiente B: "))
    c=float(input("Digite o coeficiente C: "))

    if(b == 0):
        print("A equação de segundo grau é incompleta.")
    elif(c == 0):
        print("A equação de segundo grau é incompleta.")
    else:
        delta = b * b - 4 * a * c
        
        if(delta < 0):
            print("A equação não possui raizes reais.")
        elif(delta == 0):
            x= -b / (2 * a)
            print("A equação possui apenas uma raiz real.")
            print("X =",x)
        else:
            x1 = (-b + delta ** 0.5) / (2 * a)
            x2 = (-b - delta ** 0.5) / (2 * a)

print("A equação é completa: ")
print("O valor de Delta é: ", delta)
print("O valor de X1 é: ", x1)
print("O valor de X2 é: ", x2)