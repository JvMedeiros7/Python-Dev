#Tupla: Imutável, não pode ser alterada, mas pode ser consultada. Utiliza parênteses.

'''name = ("Joao", "Maria", "Ana", "Pedro")

print(name[0])

x = 0 

for i in name:
    x += 1
    print(f"{x}: {i}")

print(name[1:3])

print(name[-1])

print(name[1:])

print(len(name))

while True:
    print("Digite um nome: ")
    n = input()
    if n in name:
        print(f"{n} encontrado!")
    else:
        print(f"{n} nao encontrado!")''',


lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")

print(lanche)