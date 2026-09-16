nasc = int(input("Digite seu ano de nascimento: "))

idade_anos = 2026 - nasc
idade_meses = idade_anos * 12
idade_semanas = idade_anos * 52
idade_dias = idade_anos * 365
idade_2019 = 2019 - nasc

print("A sua idade em anos é:", idade_anos, "anos")
print("A sua idade em meses é:", idade_meses, "meses")
print("A sua idade em semanas é:", idade_semanas, "semanas")
print("A sua idade em dias é:", idade_dias, "dias")
print("A sua idade em 2019 era:", idade_2019, "anos")