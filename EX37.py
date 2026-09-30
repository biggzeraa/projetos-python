a = float(input("Digite o valor de A: "))
if(a == 0):
    print("A equação não é de segundo grau pois A não pode ser igual a zero.")
else:
        b = float(input("Digite o valor de B: "))
        c = float(input("Digite o valor de C: "))
        delta = (b ** b) - (4 * a * c)
        if(delta < 0):
            print("A equação não possui raízes reais.")  
        elif(delta == 0):
                x = -b / (2 * a)
                print("A única raiz real é: ", x )   
        else:
            x1 = (-b + delta ** 0.5) / (2 * a)
            x2 = (-b - delta ** 0.5) / (2 * a)
            print("Os resultados são: ")
            print("X1 = ", x1)
            print("X2 = ", x2)