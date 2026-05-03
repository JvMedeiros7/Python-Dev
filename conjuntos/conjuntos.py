# Set - Elimina valores duplicados numa lista 

''' lista = [1, 2, 3, 4, 5, 5 , 6, 7, 7, 8, 8 ]

print(set(lista))

letras = set("Abacaxi")
print(letras)

repetidas = set(input("Qual valor você quer?"))
print(repetidas) ''' 

#Não suportam indexação e nem fatiamento - Caso queira Acessar os seus valores é necessário converter o conjunto para lista

''' numeros = {1,2,3,2}

numeros = list(numeros)

print(numeros[0]) ''' 

#Uso do For em set

''' carros = {"Gol" , "Celta" , "Palio" }

for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}"  ) ''' 

#Metodos de Classe do SET

#{}.union

''' conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.union(conjunto_b)) #{1, 2, 3, 4} ''' 

#{}.intersection

''' conjunto_a = {1,2, 3}
conjunto_b = {2, 3,4}

print(conjunto_a.intersection(conjunto_b)) ''' 

#{}.difference

''' conjunto_a = {1,2, 3}
conjunto_b = {2, 3,4}

print(conjunto_a.difference(conjunto_b)) #1
print(conjunto_b.difference(conjunto_a)) #4 ''' 

#{}.difference

''' conjunto_a = {1,2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b)) # 1 , 4 ''' 

#{}.issubset - Se todos de a tem em B = TRUE

''' conjunto_a = {1,2, 3}
conjunto_b = {1, 2, 3, 4}

print(conjunto_a.issubset(conjunto_b)) #True ''' 

#{}.issuperset- Se todos de B tem em A = FALSE 

''' conjunto_a = {1,2, 3}
conjunto_b = {1, 2, 3, 4}

print(conjunto_a.issuperset(conjunto_b)) #False ''' 

#{}..isdisjoint = Se os valores não se tocam = TRUE

''' conjunto_a = {1,2, 3, 4, 5 }
conjunto_b = {6, 7, 8, 9}
conjunto_C = {1,0}

print(conjunto_a.isdisjoint(conjunto_b)) #True ''' 

#{}.add - Posso passar um elemento se ele não existir é selecionado 

''' sorteio = {1, 23}

sorteio.add(25)

print(sorteio) ''' 

#{}.clear - Posso passar um elemento se ele não existir é selecionado 

''' sorteio = {1, 23}

sorteio.clear()

print(sorteio) ''' 


#{}.copy - Copia os elementos do set  

''' sorteio = {1, 23}

sorteio.copy()

print(sorteio) ''' 

#{}.discard - Descarta valores especifícos - Ignora erros - bom para erros que não gerem problemas maiores

''' numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros)

numeros.discard(1)
numeros.discard(45)

print(numeros) ''' 

#{}.pop - Descarta valores 1 a 1 

''' numeros = {1,2,3,4,5,6,7,8,9,0}

print(numeros)

print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())

print(numeros) ''' 

#{}.remove - Não ignora erros - KeyERROR se não tiver o elemento

''' numeros = {1,2,3,4,5,6,7,8,9,0}

print(numeros)

numeros.remove(2)

print(numeros) ''' 

#{}.len - Para tirar o tamanho do nosso conjunto 

''' numeros = {1,2,3,4,5,6,7,8,9,0}

print(len(numeros)) '''

#{}.in - Verificar se um elemento está dentro do conjunto

''' numeros = {1,2,3,4,5,6,7,8,9,0}

print(1 in numeros)
print(10 in numeros) ''' 