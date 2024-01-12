# Exercicio 05 - Apresentar todos os valores numéricos inteiros impares situados na faixa de 15 a 30

# Solução utilizando FOR:
for i in range(15, 31):
    if (i % 2 == 0):
        print(i)

# Solução utilizando WHILE:
i = 15
while i <= 30:
    if(i % 2 == 0):
        print(i)
    i += 1 
