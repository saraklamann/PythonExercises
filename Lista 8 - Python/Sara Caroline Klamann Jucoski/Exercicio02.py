# Exercicio 02 - Crie um programa que faça o fatorial de um número digitado

# Solução utilizando FOR:
n = int(input("Digite um número: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial = fatorial * i
print("O fatorial é", fatorial)

# Solução utilizando WHILE:
n = int(input("Digite um número: "))
fatorial = 1
i = 1
while i <= n:
    fatorial = fatorial * i
    i += 1
print("O fatorial é", fatorial)