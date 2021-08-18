#4- Faça um Programa que leia três números e mostre o maior deles.
print('#'*30)
print('maior de 3'.capitalize().center(27))
print()
n1=int(input('Digite o 1º valor: '))
n2=int(input('Digite o 2º valor: '))
n3=int(input('Digite o 3º valor: '))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f'O maior número é {maior}.')



