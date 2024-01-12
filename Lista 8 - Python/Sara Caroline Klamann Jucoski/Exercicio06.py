# Exercicio 06 - Apresentar todos os números divisíveis por 6 que sejam menores que 120

# Solução utilizando FOR:
for i in range(0, 120):
    if (i % 6 == 0):
        print(i)

# Solução utilizando WHILE:
i = 0
while i < 120:
    if(i % 6 == 0):
        print(i)
    i += 1
