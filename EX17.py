salario=int(input("Digite o seu salário: "))
salario_grat = salario + (salario * 0.05)
salario_final = salario_grat - (salario_grat * 0.07)
print("O seu salário final com a gratificação e os descontos fica: R$",salario_final)