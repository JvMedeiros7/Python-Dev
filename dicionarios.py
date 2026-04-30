#Dicionario = Conjunto não-ordenado de pares chave:valores, onde as chaves são únicas em uma dada instância do dict.
#Dicionários são delimitados por chaves: {} - Tem que ser um valor imutável 

#1. Acesso Direto (A Sintaxe Básica)

aluno = {
    "nome" : "Deivinho" , 
    "idade" : 25 , 
    "linguagem" : "Python"
}

print(aluno)
print(aluno["nome"])
print(aluno.get("stack_favorita"))

#Iterando e Imprimindo Múltiplos Valores (O Loop for)

for chave in aluno:
    print(f"A chave {chave} guarda o valor: {aluno[chave]}")

#Opção B: Extraindo apenas os valores diretamente (Mais eficiente)

for valor in aluno.values():
    print(valor)

#Opção C: Extraindo Chave e Valor simultaneamente

for chave, valor in aluno.items():
    print(f"Propriedade: {chave} | Dado: {valor}")