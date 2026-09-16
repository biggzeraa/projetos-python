tempo=input("Digite o seu período: (M = Matutino, V = Vespertino e N = Noturno.) ").lower()

if(tempo == "m"):
    print("Bom dia. O seu período é Matutino!")

elif(tempo == "v"):
    print("Boa tarde. O seu período é Vespertino!")

elif(tempo == "n"):
    print("Boa noite. O seu perído é Noturno!")

else:   
    print("O seu perído é inválido, tente novamente.")