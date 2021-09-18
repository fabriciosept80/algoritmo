#3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20
# elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
# Imprima os três vetores.

from random import randint
print('*'*30)
print('LISTA INTERCALADA'.center(30))
print()
lista_A = list()
lista_B = list()
lista_AB = list()
count = 0
for x in range(0,10):
    lista_A.append(randint(1,100))
    lista_B.append(randint(1,100))
while count < len(lista_B):
    lista_AB.append(lista_A[count])
    lista_AB.append(lista_B[count])
    count += 1
print(f'Os valores gerados da lista_A são {lista_A} no total de {len(lista_A)} elementos.' )
print(f'Os valores gerados da lista_B são {lista_B} no total de {len(lista_B)} elementos.' )
print(f'A lista de A + B intercalada é {lista_AB} com {len(lista_AB)} elementos.')