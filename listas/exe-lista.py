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

'''L = list(range(101))

del L[1:99]

print(L)'''

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

    indice = 0 

    while indice < len(operacao):
        tipo = operacao[indice]
        print(tipo)
        indice += 1 
            if tipo == "A":
                if len(fila) > 0:
                    atendido = fila.pop(0)
                    print(f"Cliente {atendido} atendido")
                else:
                print(f"Fila vazia! Ningúem para me atender.")
            elif tipo == "F": 
                ultimo += 1
                fila.append(ultimo)
            elif operacao == "S":
                break
            else:
                print("Operação invalida! Digite apenas F,A ou S!")
                

'''ultimo = 10
fila = list(range(1, ultimo + 1))

rodando = True

while rodando:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("Ou A para realizar o atendimento. S para sair.")
    
    # Boas práticas: o .upper() garante que, se o usuário digitar 'ffaa',
    # o sistema não quebre por ser case-sensitive.
    operacao = input("Operação(F, A ou S): ").upper()

    indice = 0 

    # Enquanto houver caracteres na string 'operacao' para ler...
    while indice < len(operacao):
        tipo = operacao[indice]
        print(f"\n--- Processando comando: {tipo} ---")
        
        # Correção 1: Uso do '==' para comparação.
        # Correção 2: Indentação perfeitamente alinhada para a estrutura if-elif-else (Aula 06).
        if tipo == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)  # Remove o primeiro da fila (índice 0)
                print(f"Cliente {atendido} atendido.")
            else:
                # Este 'else' pertence estritamente ao 'if len(fila) > 0'
                print("Fila vazia! Ninguém para ser atendido.")
                
        elif tipo == "F": 
            ultimo += 1
            fila.append(ultimo)
            print(f"Cliente {ultimo} entrou na fila.")
            
        elif tipo == "S":
            # Correção 3: Verificamos 'tipo' e alteramos a flag do loop principal.
            print("Encerrando o programa...")
            rodando = False
            break  # Interrompe o loop interno imediatamente. O loop externo não reiniciará pois rodando = False.
            
        else:
            print(f"Operação inválida ({tipo}) ignorada! Use apenas F, A ou S.")
            
        # O incremento do índice deve ficar fora das condições, para sempre avançar para a próxima letra.
        indice += 1 '''           