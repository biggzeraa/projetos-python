num=int(input("Digite o número para consultar a tabuada: "))
print("\nA tabuada do número ", num , " é:")
for i in range(1, 11):
    resultado = num * i
    print("\n", num,"x" ,i, " = ", resultado, "\n")
