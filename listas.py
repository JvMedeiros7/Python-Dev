#Listas em Python

''' frutas = [ "Laranja" , "Maça" , "Uva"]
print(frutas)
print(frutas[0])
print(frutas[-1])

frutas = []
print(frutas)

letras = list("Python")
print(letras)
print(letras[0])
print(letras[-1])

numeros = list(range(10))
print(numeros)
print(numeros[0])
print(numeros[-1])

carro = [ "Ferrari" , "F8" , 42000 , 2020 , 2900 , "São Paulo" , True ]
print(carro)
print(carro[0])
print(carro[-1]) ''' 

#Matriz em Python

'''
 matriz = [
    [1, "a" , 2],
    ["b" , 3 , 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print([0][-1])
print([-1][-1]) '''

''' lista = ["p" , "y" , "t" , "h" , "o" , "n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

['t', 'h', 'o', 'n']
['p', 'y']
['y', 't']
['p', 't']
['p', 'y', 't', 'h', 'o', 'n']
['n', 'o', 'h', 't', 'y', 'p'] ''' 

#Forma de mostrar os elementos da lista padrão 

''' carros = ["Gol" , "Celta" , "Palio"]

for carro in carros:
    print(carro) ''' 

# Quando for necessário saber qual o índice do objeto dentro do laço FOR - Usamos a função Enumerate

''' carros = ["Gol" , "Celta" , "Palio"]

for indice, carro in  enumerate(carros):
    print(f"{indice} : {carro}") ''' 

#Compreensao de Listas - Criar nova lista com base nos valores de uma lista existente

''' numeros = [1, 30 , 21 ,2 , 9 , 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares) '''

#Compreensao de Listas - Versão Python

''' numeros = [1, 30 , 21 ,2 , 9 , 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares) ''' 

#Modificando valores - v1

''' numeros = [1, 30, 21 ,2 ,9 , 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2) ''' 


#Modificando valores - Versão Python

''' numeros = [1, 30, 21 ,2 ,9 , 65, 34]
quadrado = [ numero ** 2 for numero in numeros]

print(f"O número {numeros[0]} ao quadrado é {quadrado[0]}") ''' 


#Metodo para adicionar novo elemento na lista - []. Append

''' lista = []
lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista)
[1, 'Python', [40, 30, 20]] ''' 


#Metodo para limpar a lista - [].clear

''' lista = [1, "Python" , [40, 30, 20]]

print(lista)
[1, 'Python', [40, 30, 20]]

lista.clear()

print(lista)
[] ''' 

#Para copiar uma lista 

''' lista = [1, "Python" , [40, 30, 20]]

l2 = lista.copy()

print(lista)

print(id(l2) , id(lista))

l2[0] = 2 

#Conseguimos uma copia com os mesmos valores, mas podemos modificar sem alterar a lista original.

print(l2)
print(lista) ''' 

#Para contar a quantiadade que um objeto aparece na lista = [].count

''' cores = ["Vermelho" , "Azul" , "Verde" , "Azul"]
       
print(cores.count("Vermelho")) - 1 
print(cores.count("Azul")) - 2 ''' 

#Para passar uma 2a lista e juntar ela com a 1a = [].extend

''' linguagens = ["Python" , "Js" , "c"]

print(linguagens)
['Python', 'Js', 'c']

linguagens.extend(["Java" , "C"])

print(linguagens)
['Python', 'Js', 'c', 'Java', 'C'] ''' 

#Para saber onde é a 1a ocorrência do objeto - primeira vez onde ele vai aparecer = [].index

''' linguagens = ["Python" , "js" , "c" , "Java" , "csharp"]

print(linguagens.index("Java"))
print(linguagens.index("Python")) ''' 

#Tira o último elemento adicionado na lista = [].pop

''' linguagens = ["Python" , "Js" , "C" , "Java" , "csharp"]

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())

#Pode-se usar para tirar elementos nos indices especificados
print(linguagens.pop(0))

print(linguagens) ''' 

# Remover elementos de uma lista = [].remove

''' linguagens = ["Python" , "Js" , "C" , "Java" , "Csharp"]

linguagens.remove("Python")

print(linguagens) ''' 

# Deixar a lista ao contrário do ÚLTIMO INDICE para o primeiro = [].reverse

''' linguagens = ["Python" , "Js" , "C" , "Java" , "Csharp"]

linguagens.rever()

print(linguagens) ''' 

# Ordena a lista em ordem alfabêtica

''' linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

#Ordena por tamanho da palavra :

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens) ''' 

# Para ver o tamanho dos objetos = [].len

''' linguagens = ["Python" , "Js" , "c" , "Java" , "csharp"]

print(len(linguagens)) # 5   
print(len(linguagens[0])) #6 ''' 
 
# Serve para ordenar iteráveis = [].sorted

''' linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"] ''' 


#Livro Python

'''z = [15 , 8 , 9]

print(z[0])

z[0] = 7 

print(z[0])'''

#Programa 6.2: Cálculo da média com notas digitadas

'''notas = [0, 0, 0, 0, 0, 0]
soma = 0 
x = 0 

while x < 6:
    notas[x] = float(input(f"Nota {x}:"))
    soma += notas[x]
    x += 1

x = 0 

while x > 6:
    print(f"Nota {x} : {notas[x]:6.2f}")
    x +=1 
 
print(f"media: {soma / len(notas):.2f}")'''

#Programa 6.3: Apresentação de Números

numeros = [0, 0, 0, 0, 0]
x = 0

while x < 5:
    numeros[x] = int(input(f"Números {x+1}:"))
    x += 1
while True:
    escolhido = int(input("Que posição você quer imprimir(0 para sair):"))
    if escolhido == 0:
        break
    print (f"Você escolheu o número: {numeros[escolhido - 1]}")