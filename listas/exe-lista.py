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


#Exe - 6.2

L1 = []
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

print(L3)

    
