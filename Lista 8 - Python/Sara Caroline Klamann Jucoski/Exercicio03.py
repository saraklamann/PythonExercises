# Exercicio 04 - Crie um programa que leia o nome do vendedor, total de vendas e some o total de vendas com 25% de comissão
nome_vendedor = str(input("Digite o nome do vendedor: "))
numero_de_vendas = int(input("Digite o número de vendas realizadas: "))

valor_venda = 0
valor_total_vendas = 0

for i in range(0, numero_de_vendas):
    valor_venda = float(input(f"Digite o valor da {i + 1}° venda: "))
    valor_total_vendas = valor_total_vendas + valor_venda
valor_comissao = valor_total_vendas * 0.25

print(f"O vendedor {nome_vendedor} vendeu {valor_total_vendas} reais e recebeu {valor_comissao} reais de comissão.")

# print(f"Dados do(a) vendedor(a) {nome_vendedor}:")
# print("Quantidade de vendas: {} \n \
#     Valor total vendido: R$ {:.2f} \n \
#     Valor de comissão recebido: R$ {:.2f}".format(numero_de_vendas, valor_total_vendas, valor_comissao))