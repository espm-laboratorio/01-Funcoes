
# função para imprimir a lista
def imprimir(lista: list[int]) -> None:
    for i in lista:
        print(f"{i}", end=" ")

# função para verificar se um número é primo
def eh_primo(valor: int) -> bool:
    if valor < 2:
        return False
    for i in range(2, int(valor**0.5)+1):
        if valor % i == 0:
            return False
    return True

# função para gerar n números primos
def gerar_primos(n: int) -> list:
    lista = []
    valor = 2
    while len(lista) < n:
        if eh_primo(valor):
            lista.append(valor)
        valor = valor + 1
    return lista


# função main
def main() -> None:
    n = int(input("Informe a quantidade de números primos: "))
    lista = gerar_primos(n)
    imprimir(lista)

# programa principal
if __name__ == '__main__':
    main()