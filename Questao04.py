estoque = 0
pedido = int(input("Informe a quantidade desejada: "))

if(estoque == 0):
    producao = pedido * 2
    print("O número de tacos fabricados é de: ", producao)
    estoque = producao - pedido
else: 
    print("O número de tacos fabricados é de: ", pedido)
    estoque = pedido
