#Exe - 6.2

'''L1 = []
x = 0 

while True:
    n = float(input(f"({x+1}). DIGITE O VALOR GASTO PARA A LISTA 1 R$ (0 PARA SAIR):  "))
    x += 1
    if n == 0:
        break
    L1.append(n)

L2 = []
x = 0

while True:
    n = float(input(f"({x+1}). DIGITE O VALOR GASTO PARA A LISTA 2 R$ (0 PARA SAIR):  "))
    x += 1
    if n == 0:
        break
    L2.append(n)

#Somamos os elementos
S = L1 + L2
print(S)


#Somamos a lista como 1 elemento
L1.append(L2)

print(L1) '''


#Exe - 6.3

'''L1 = []
x = 0 

while True:
    n = float(input(f"({x+1}). DIGITE O VALOR PARA A LISTA 1 (0 PARA SAIR):  "))
    x += 1
    if n == 0:
        break
    L1.append(n)

L2 = []
x = 0

while True:
    n = float(input(f"({x+1}). DIGITE O VALOR PARA A LISTA 2 (0 PARA SAIR): "))
    x += 1
    if n == 0:
        break
    L2.append(n)
    
L3 = []

for x in L1:
    if x not in L3:
        L3.append(x)

for y in L2:
    if y not in L3:
        L3.append(y)

print(L3)'''

#Instrução del 

L = list(range(101))

del L[1:99]

print(L)

#Metodo pop = .pop() = Retorna o valor do elemento e o exclui da fila

#Programa 6.7: Simulação de uma fila de banco

'''ultimo = 10
fila= list(range(1,ultimo + 1))

while True:
    print(f"\n Existem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("Ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação(F , A ou S):")
    if operacao == "A":
        if len(fila) >0:
            atendido = fila.pop(0)
            print(f"Cliente{atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")
    
    elif operacao == "F":
        ultimo += 1 #Incremento o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")'''


#Exe 6.5: Simulação de uma fila de banco

ultimo = 10
fila= list(range(1,ultimo + 1))

while True:
    print(f"\n Existem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("Ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação(F , A ou S):")


    if operacao == str("A"):
        if len(fila) >0:
            atendido = fila.pop(0)
            print(f"Cliente{atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")

    
    elif operacao == str("F"):
        ultimo += 1 #Incremento o ticket do novo cliente
        fila.append(ultimo)


    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")
        
        