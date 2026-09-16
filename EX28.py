N1=int(input("digite o seu primeiro numero:"))
N2=int(input("digite o seu segundo numero:"))
N3=int(input("digite o seu terceiro numero:"))
maior=N1
if(N2>maior):
    maior=N2
elif(N3>maior):
    maior=N3
print("\nO amior numero é:",maior)