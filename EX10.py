lado1=int(input("Informe o primerio lado do triângulo:"))
lado2=int(input("Informe o segundo lado do triângulo:"))
lado3=int(input("Informe o terceiro lado do triângulo:"))

(lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)
    
if(lado1 == lado2 == lado3):
    print("Seu triângulo é equilátero")
elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print("É um triângulo Isósceles (dois lados iguais).")
else:
    print("É um triângulo Escaleno (três lados diferentes).")