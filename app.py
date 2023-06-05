def busca_numero(vetor, x):
    for i in range(len(vetor)):
        if vetor[i] == x:
            return i  # Retorna o índice onde o número foi encontrado
    return -1  # Retorna -1 se o número não foi encontrado no vetor


# Exemplo de uso
numeros = [4, 8, 15, 16, 23, 42]
numero_buscar = 16

indice = busca_numero(numeros, numero_buscar)

if indice != -1:
    print(
        f"O número {numero_buscar} foi encontrado no \
        índice {indice} do vetor.")
else:
    print(f"O número {numero_buscar} não foi encontrado no vetor.")
