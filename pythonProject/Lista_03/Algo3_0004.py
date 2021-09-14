#4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples:
# os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo
# que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2.
print('*'*53)
print('Descobrindo o número Fibonacci pela posição digitada'.title())
a = b = 1
c = count = 0
n= int(input('Digite um numero: '))
while count < n:#>>n-2
    a = b
    b = c
    c = a + b
    #a,b = b, a + b # jeito do professor.
    count += 1
print(f'O número {n} corresponde a {c} na sequencia Fibonacci.')

