aior = float('-inf')

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    if numero > maior:
        maior = numero

print("O maior número é:", maior)
