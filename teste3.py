palavra=input("Digite uma palavra: ")
print(f'{palavra.upper()} e tem {len(palavra)} de letras')
palavra = palavra + palavra [::-1]
print(palavra)
print(palavra.split(' '))