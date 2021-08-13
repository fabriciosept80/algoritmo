#5-Faça um Programa que leia três números e mostre o maior e o menor deles.
print('#'*30)
print('Maior e Menor de 3'.center(27))
print()
n1=int(input('Digite o 1º valor: '))
n2=int(input('Digite o 2º valor: '))
n3=int(input('Digite o 3º valor: '))
print(f'O maior valor dentre os valores digitados é : {max(n3,n2,n1)}')
print(f'O menor valor dentre os valores digitados é : {min(n3,n2,n1)}')
