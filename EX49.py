num = int(input("Digite o numero pra descobrir na serie de finobacci: "))
fib = 1
ant = 0
seq = 1

print(fib, end=", ")

while seq != num:
    prox = fib + ant
    ant = fib
    fib = prox
    print(fib, end=", ")
    seq += 1