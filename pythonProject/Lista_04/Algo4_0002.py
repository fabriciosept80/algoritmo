#2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista
# IMPAR. Imprima as três listas.

from random import randint
print('*'*60)
print('Lista de Pares e Ímpares'.center(60))
print()
numero = []
par = list()
impar = list()
for a in range (0,20):
    numero.append(randint(1,100))
    if numero[a] % 2 == 0:
        par.append(numero[a])
    else:
        impar.append(numero[a])
print(f'Na lista {numero} os números pares são \n \033[1;36m{par}\033[m e os ímpares são \033[1;32m{impar}\033[m')
print()
print(f'Total de números pares: \033[1;36m{len(par)}\033[m')
print(f'Total de números ímpares: \033[1;32m{len(impar)}\033[m')