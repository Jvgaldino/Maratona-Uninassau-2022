C = int(input("Informe a quantidade de competidores: "))
P = int(input("Informe a quantidade de folhas de papel compradas: "))
F = int(input("Informe a quantidade de folhas de papel que cada competidor deve receber: "))

if (C * F <= P):
    print("S")
    
else:
    print("N")
