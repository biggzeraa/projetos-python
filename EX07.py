n1=int(input("Digite a primeira nota: "))
n2=int(input("Digite a segunda nota: "))
n3=int(input("Digite a terceira nota: "))
n4=int(input("Digite a quarta nota: "))
disc=input("Digite o nome da Disciplina: ")

media = (n1 + n2 + n3 + n4) / 4

if(media >= 7):
    print("Parabéns! Você está na média com a nota: ",media ,"na matéria de: ", disc)
else:
    print("Você não passou! Sua média foi: ", media ,"na matéria de: ", disc)