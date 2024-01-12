# Exercicio 08:

def pedir_valores(i):
    n = float(input(f"Digite o {i}° valor: "))
    return n

def verificar_valores(n2):
    if n2 == 0:
        valido = False
    else:
        valido = True
    return valido

def encontrar_maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        maior = n1
    elif n2 > n1 and n2 > n3:
        maior = n2
    else:
        maior = n3
    return maior
    
def encontrar_menor(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        menor = n1
    elif n2 < n1 and n2 < n3:
        menor = n2
    else:
        menor = n3
    return menor

def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

def mostrar_resultados(n1, n2, n3):
        print("A soma dos valores informados é", (n1 + n2 + n3))
        print("A subtração do primeiro pelo segundo valor é", (n1 - n2))
        if verificar_valores(n2) == True:
            print("A divisão do terceiro pelo segundo valor é", (n3 / n2))
        else:
            print("Não é possivel realizar a divisão pois o segundo número é zero")
        print("A multiplicação do primeiro pelo segundo valor é", (n1 * n2))
        print(f"O maior valor digitado foi {encontrar_maior(n1,n2,n3)}")
        print(f"O menor valor digitado foi {encontrar_menor(n1,n2,n3)}")
        print(f"A média dos valores informados é {calcular_media(n1, n2, n3)}")

def main():
    n1 = pedir_valores(1)
    n2 = pedir_valores(2)
    n3 = pedir_valores(3)

    print("Os resultados são:")
    mostrar_resultados(n1, n2, n3)
    
main()