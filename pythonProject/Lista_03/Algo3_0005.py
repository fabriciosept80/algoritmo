#5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
print('*'*30)
print('Euclides'.center(30))
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
um = n1
zero = n2
while (n1 != 0):
    if n2 == 0:
        break
    else:
        x = n1 % n2
        n1 = n2
        n2 = x
if zero != 0:
    print(f'O MDC entre {um} e {zero} é {n1}')
else:
    print('Não é possível dividir por 0')
