# Exercicio 04 - Apresentar o total da soma obtida dos cem primeiros números inteiros

# Solução utilizando FOR:
soma = 0
for i in range(1, 101):
    soma = soma + i
print(soma)

# Solução utilizando WHILE:
soma = 0
i = 1
while i <= 100:
    soma += i
    i += 1
print(soma)