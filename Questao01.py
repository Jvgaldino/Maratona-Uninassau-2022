M = int(input("Insira a idade da mãe: "))
A = int(input("Insira a idade do filho A: "))
B = int(input("Insira a idade do filho B: "))

#para saber a idade do terceiro filho
C = M-A-B
#para saber qual a idade maior dos 3
C = max(C,A,B)

print("A idade do mais velho é: ", C )
        