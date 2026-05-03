#Exe - 6.2

L1 = []
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

S = L1 + L2
print(S)

L1.append(L2)

print(L1)


