#Desafio 078

'''numeros = list()

x = 0
for valor in range(0,5):

    numeros.append(int(input(f'Digite um valor na posição {x}: ')))
    x += 1
print(f'Você digitou os valores {numeros}')

print(f'O maior valor digitado foi {max(numeros)} na posição {numeros.index(max(numeros))}')
print(f'O menor valor digitado foi {min(numeros)} na posição {numeros.index(min(numeros))}')'''

#Desafio 079

'''valores = list()
soma = 0

while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += valores[-1]
    if resposta in 'N':
        break
print(f'Você digitou os valores {sorted(valores)}')
print(f'A soma dos valores digitados é {soma}')'''

#Desafio 080

numeros = list()

for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1

print(f'Os valores digitados em ordem são: {numeros}')
