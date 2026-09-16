deposito=int(input("Digite o valor do depósito: "))
juros=int(input("Digite o valor da taxa de juros: (em porcentagem) "))
jurosfinais = deposito + (deposito * juros / 100)
print("O valor do depósito com os juros ficaria: R$", jurosfinais)