
# função para calcular o total de grãos
def calcular() -> int:
    total  = 0
    for i in range(64):
        total += 2 ** i
    return total
    

# programa principal
total = calcular()
print(f"total de grãos: {total}")
print()