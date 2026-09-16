n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
oper=(input("Selecione a operação (S = Soma e Sub = Subtração.) "))

if (oper == "S"):
    soma = (n1+n2)
    print("O resultado da soma é: ",soma)

elif (oper == "Sub"):
    sub = (n1-n2)
    print("O resultado da subtração é: ",sub)

else:
    print("Operação inválida, tente novamente.")