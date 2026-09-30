m=float(input("Digite o valor da área que será pintada: "))
litros = m / 3
latas = int(litros / 18)
if(latas % 18 != 0):
    latas += 1

    valor = latas * 80

    print("\nPara a sua área de: ", m ," Metros quadrados foram necessários: \n")
    print(latas, " Latas de tinta\n")
    print(round(litros, 2), " Litros de tinta\n")
    print("E o valor para cobrir a área total foi de: ", valor , " Reais.")