#Exercicio 5.1 

''' x = 1 
while x <= 100:
    print(x)
    x = x + 1  ''' 

#Exercicio 5.2

''' x = 50
while x <= 100:
    print(x)
    x = x + 1  ''' 

#Exercicio 5.3

''' x = 10
while x >= 1:
    print(f" A conta regressiva está em {x} !!!!")
    x = x - 1  ''' 

#Exercicio 5.4

''' fim = int(input("Digite o último número a imprimir:"))
x = 1 
while x <= fim:
    print (x)
    x = x + 2  ''' 

#Exercicio 5.5

''' x = 3 
while x <= 30:
    print (x)
    x = x + 3 ''' 

#Exercicio 5.6.7.

''' n = int(input("Tabuada de:"))
limite = int(input("Digite o n° de até onde vai ser a tabuada?"))
x = 1 
while x <= limite:
    tabuada = n * x 
    print(f"O resultado da tabuada é {x} x {n} = {tabuada}")
    x = x + 1  ''' 

#Exercicio 5.8 

''' n1 = int(input("Digite o n1: "))
n2 = int(input("Digite o n2: "))

soma = 0  
contador = 1  


while contador <= n2:
    soma = soma + n1  
    contador = contador + 1 

print(f"O resultado de {n1} x {n2} é: {soma}") ''' 

#Exercicio 5.9 

''' dividendo = int(input("Digite o dividendo (n1): "))
divisor = int(input("Digite o divisor (n2): "))


n1 = dividendo
n2 = divisor

quociente = 0
resto = n1

# Enquanto o que sobrou for maior ou igual ao divisor...
while resto >= n2:
    resto = resto - n2  # Subtraímos o divisor
    quociente = quociente + 1  # Contamos quantas vezes subtraímos

print("-" * 30)
print(f"Dividindo {n1} por {n2}:")
print(f"Quociente (divisão inteira): {quociente}")
print(f"Resto da divisão: {resto}")  ''' 

#Exercicio 5.10

''' pontos = 0 
q = 1

while q <= 3:
    res = input(f"Resposta da questão {q}: ").strip().upper()
    
    if q == 1 and res == "B":
        pontos += 1 
    elif q == 2 and res == "A":
        pontos += 1 
    elif q == 3 and res == "C":
        pontos += 1
        
    q += 1 

print("-" * 20)
print(f"Resultado final: {pontos} ponto(s).") ''' 
