n1=float(input("Digite o primeiro número: "))
n2=float(input("Digite o segundo número: "))
oper=input("Digite a operação desejada: \n(Soma = +  Subtração = -  Divisão = /  Multiplicação = *)\n").lower()

if(oper == "+"):
    print("O resultado da soma é: ", n1+n2)
elif(oper == "-"):
    print("O resultado da subtração é: ", n1-n2)
elif(oper == "*"):
    print("O resultado da multiplicção é: ", n1*n2)
elif(oper == "/"):
    print("O resultado da divisão é: ", n1/n2)
else:
    print("A operação não existe, tente novamente.")