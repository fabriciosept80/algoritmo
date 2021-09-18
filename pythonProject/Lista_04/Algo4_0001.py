# 1 - Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.

from random import randint
print('*'*60)
print('Sorteio de números inteiros => Maior e Menor'.center(60))
numeros = list()
for a in range(0, 10):
    numeros.append(randint(1, 100))
    if a == 0:
        maior = menor = numeros[a]
    else:
        if maior < numeros[a]:
            maior = numeros[a]
        if menor > numeros[a]:
            menor = numeros[a]

print(f'O maior valor da lista {numeros} é: {maior}')
print(f'O menor valor da lista {numeros} é: {menor}')


