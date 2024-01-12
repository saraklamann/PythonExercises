# Exercicio 07 - Apresentar o valor do somatório de todos os valores pares existentes entre 100 e 200

# Solução utilizando FOR:
soma = 0
for i in range(100, 201, 2): 
    soma = soma + i
print(soma)

# Solução utilizando FOR:
soma = 0
i = 100
while i <= 200:
    soma += i
    i += 2
print(soma)