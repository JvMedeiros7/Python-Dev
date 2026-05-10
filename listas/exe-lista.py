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
        indice += 1        ''' 


#Exe 6.5: Simulação de uma fila de banco

'''ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))


rodando = True

while rodando:
    print(f"\nExistem {len(fila1)} e {len(fila2)}clientes na fila.")
    print(f"Fila 1 atual: {fila1}  - Fila 2 atual: {fila2} ")
    filadesejada = input("Você deseja atender na fila 1 (A) ou na fila 2 (B):").upper()

    if filadesejada == "A":

        print("Digite F para adicionar um cliente ao fim da fila 1,")
        print("Ou A para realizar o atendimento. S para sair.")
    
    # Boas práticas: o .upper() garante que, se o usuário digitar 'ffaa',
    # o sistema não quebre por ser case-sensitive.
        operacao1 = input("Operação(F, A ou S): ").upper()

        indice1 = 0 

    # Enquanto houver caracteres na string 'operacao' para ler...
        while indice1 < len(operacao1):
            tipo1 = operacao1[indice1]
            print(f"\n--- Processando comando: {tipo1} ---")
        
        # Correção 1: Uso do '==' para comparação.
        # Correção 2: Indentação perfeitamente alinhada para a estrutura if-elif-else (Aula 06).
            if tipo1 == "A":
                if len(fila1) > 0:
                    atendido1 = fila1.pop(0)  # Remove o primeiro da fila (índice 0)
                    print(f"Cliente {atendido1} atendido.")
                else:
                # Este 'else' pertence estritamente ao 'if len(fila) > 0'
                    print("Fila vazia! Ninguém para ser atendido.")
                
            elif tipo1 == "F": 
                ultimo1 += 1
                fila1.append(ultimo1)
                print(f"Cliente {ultimo1} entrou na fila.")
            
            elif tipo1 == "S":
            # Correção 3: Verificamos 'tipo' e alteramos a flag do loop principal.
                print("Encerrando o programa...")
                rodando = False
                break  # Interrompe o loop interno imediatamente. O loop externo não reiniciará pois rodando = False.
            
            else:
                print(f"Operação inválida ({tipo1}) ignorada! Use apenas F, A ou S.")
            
        # O incremento do índice deve ficar fora das condições, para sempre avançar para a próxima letra.
            indice1 += 1 

#Bloco fila 2 

    elif filadesejada == "B":     
        print("Digite F para adicionar um cliente ao fim da fila 1,")
        print("Ou A para realizar o atendimento. S para sair.")
    
    # Boas práticas: o .upper() garante que, se o usuário digitar 'ffaa',
    # o sistema não quebre por ser case-sensitive.
        operacao2 = input("Operação(F, A ou S): ").upper()

        indice2 = 0 

    # Enquanto houver caracteres na string 'operacao' para ler...
        while indice2 < len(operacao2):
            tipo2 = operacao2[indice2]
            print(f"\n--- Processando comando: {tipo2} ---")
        
        # Correção 1: Uso do '==' para comparação.
        # Correção 2: Indentação perfeitamente alinhada para a estrutura if-elif-else (Aula 06).
            if tipo2 == "A":
                if len(fila2) > 0:
                    atendido2 = fila2.pop(0)  # Remove o primeiro da fila (índice 0)
                    print(f"Cliente {atendido2} atendido.")
                else:
                # Este 'else' pertence estritamente ao 'if len(fila) > 0'
                    print("Fila vazia! Ninguém para ser atendido.")
                
            elif tipo2 == "F": 
                ultimo2 += 1
                fila2.append(ultimo2)
                print(f"Cliente {ultimo2} entrou na fila.")
            
            elif tipo2 == "S":
            # Correção 3: Verificamos 'tipo' e alteramos a flag do loop principal.
                print("Encerrando o programa...")
                rodando = False
                break  # Interrompe o loop interno imediatamente. O loop externo não reiniciará pois rodando = False.
            
            else:
                print(f"Operação inválida ({tipo2}) ignorada! Use apenas F, A ou S.")
            
        # O incremento do índice deve ficar fora das condições, para sempre avançar para a próxima letra.
            indice2 += 1 
'''


'''#Exe 6.5: Simulação de uma fila de banco

ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))

rodando = True

while rodando:
    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} clientes na fila 2.")
    print(f"Fila 1 atual: {list(fila1)}  -  Fila 2 atual: {list(fila2)}")
    print("\nDigite:")
    print("[F] Chegada Fila 1  | [G] Chegada Fila 2")
    print("[A] Atender Fila 1  | [B] Atender Fila 2")
    print("[S] Sair do Sistema")
    
    operacao = input("-> Operação(ões): ").upper()

    indice = 0 

    # Enquanto houver caracteres na string 'operacao' para ler...
    while indice < len(operacao):
        tipo = operacao[indice]
        print(f"\n--- Processando comando: {tipo} ---")
        
        # Correção 1: Uso do '==' para comparação.
        # Correção 2: Indentação perfeitamente alinhada para a estrutura if-elif-else (Aula 06).
        if tipo == "A":
            if len(fila1) > 0:
                atendido1 = fila1.pop(0)  # Remove o primeiro da fila (índice 0)
                print(f"Cliente {atendido1} atendido.")
            else:
                # Este 'else' pertence estritamente ao 'if len(fila) > 0'
                print("Fila vazia! Ninguém para ser atendido.")
        elif tipo == "B":
            if len(fila2) > 0:
                atendido2 = fila2.pop(0)  # Remove o primeiro da fila (índice 0)
                print(f"Cliente {atendido2} atendido.")
            else:
                # Este 'else' pertence estritamente ao 'if len(fila) > 0'
                print("Fila vazia! Ninguém para ser atendido.")
                
        elif tipo == "F": 
            ultimo1 += 1
            fila1.append(ultimo1)
            print(f"Cliente {ultimo1} entrou na fila.")
        
        elif tipo == "G": 
            ultimo2 += 1
            fila2.append(ultimo2)
            print(f"Cliente {ultimo2} entrou na fila.")

        elif tipo == "S":
            # Correção 3: Verificamos 'tipo' e alteramos a flag do loop principal.
            print("Encerrando o programa...")
            rodando = False
            break  # Interrompe o loop interno imediatamente. O loop externo não reiniciará pois rodando = False.  
        else:
            print(f"Operação inválida ({tipo}) ignorada! Use apenas F, G, A, B ou S.")
            # O incremento do índice deve ficar fora das condições, para sempre avançar para a próxima letra.
        indice += 1   '''     


'''# Programa 6.8: Pilha de Pratos

prato = 5
pilha = list(range(1, prato + 1))

while True:
    print(f"\n existem {len(pilha)} pratos na pilha.")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar um novo prato,")
    print("Ou D para desempilhar. S para Sair.")

    operação = input("Operação (E, D OU S): ")
    if operação == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha Vazia! Nada para lavar.")
    elif operação == "E":
        prato += 1
        pilha.append(prato)
    elif operação == "S":
        break
    else:
       print("Operação inválida! Digite apenas E,D ou S!")'''


''' #Estrutura de dados / Leitura

expressao = "(a+b)"
x = 0

# 1. CRIANDO A ESTRUTURA DE CONTROLE
# Criamos uma lista vazia. É ela quem tem permissão para usar .append() e .pop()[cite: 1].
pilha = []

while x < len(expressao):
    # Apenas LÊ a informação na posição x. Não alteramos essa variável.
    caractere_atual = expressao[x]
    
    # --- ÁREA DA REGRA DE NEGÓCIO ---
    
    if caractere_atual == "(":
        # Achamos uma abertura. Colocamos um "prato" na nossa lista.
        pilha.append("(") 
        
    elif caractere_atual == ")":
        # Achamos um fechamento. Retiramos o último "prato" da nossa lista[cite: 1].
        pilha.pop()
        
    # --------------------------------
    
    # Motor do laço
    x += 1 

# Fim da varredura.

(()) Ok
()()(()()) Ok
()) Erro'''


'''# Expressões de teste baseadas no seu escopo
exp_1 = "(())"          # Esperado: Ok
exp_2 = "()()(()())"    # Esperado: Ok
exp_3 = "())"           # Esperado: Erro (Tenta desempilhar pilha vazia)
exp_4 = "(()"           # Esperado: Erro (Sobra elemento na pilha)

expressao = exp_3 # Troque a variável aqui para testar os outros casos

# 1. Inicializamos a nossa "Pilha" usando uma lista vazia
pilha = []

# 2. Todo 'while' precisa de uma variável de inicialização para o controle
i = 0 

# Variável de controle de estado (flag) para saber se a expressão quebrou a regra
valida = True

# 3. O 'while' repete o bloco enquanto o índice 'i' for menor que o tamanho da string
while i < len(expressao):
    caractere = expressao[i] # Acessamos o caractere na posição atual do índice
    
    if caractere == '(':
        # REGRA 1: Sempre que encontrar '(', adiciona (empilha) ao final da lista[cite: 9]
        pilha.append(caractere)
        
    elif caractere == ')':
        # REGRA 2: Encontrou ')'. Antes de dar o pop(), verificamos o tamanho da lista[cite: 9]
        # Isso previne o erro fatal de tentar desempilhar uma lista vazia.
        if len(pilha) > 0:
            pilha.pop() # Remove o último elemento inserido (desempilha)[cite: 9]
        else:
            # Se a pilha está vazia e chegou um ')', a ordem está errada.
            valida = False
            break # Interrompe o loop manualmente, pois já identificamos o erro fatal[cite: 8]
            
    # 4. Todo 'while' precisa da atualização da variável para não gerar loop infinito[cite: 8]
    i += 1 

# 5. Avaliação Fria do Estado Final
# A expressão só é correta se não quebrou a regra no meio (valida == True) 
# E se, no final de tudo, não sobrou nenhum '(' perdido (len(pilha) == 0)
if valida and len(pilha) == 0:
    print(f"A expressão '{expressao}' está: Ok")
else:
    print(f"A expressão '{expressao}' está: Erro")'''

# Desejado


expressão = input("Digite a sequência de parênteses a validar:")
x = 0
pilha = []
while x < len(expressão):
    if expressão[x] == "(":
        pilha.append("(")
    if expressão[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")  # Força a mensagem de erro
            break
    x = x + 1
if len(pilha) == 0:
    print("OK")
else:
    print("Erro")