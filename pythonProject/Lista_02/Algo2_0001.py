# 1-  Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem
# ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno

def type_tri(n1,n2,n3):
    if n1 == n2 == n3:
        return "Equilatero"
    if n1 == n2 or n1 == n3 or n2 == n3:
        return "Isosceles"
    if n1 != n2 != n3:
        return  "Escaleno"

print('*'*40)
print('Verificação do Triangulo')
print()
n1=int(input('Entre com o valor 1: '))
n2=int(input('Entre com o valor 2: '))
n3=int(input('Entre com o valor 3: '))
if ((n1 + n2) > n3 and (n1 + n3) > n2) and (n3 + n2) > n1:
    print(f'As medidas {n1}, {n2} e {n3} formam um triangulo',end=' - ')
    print(type_tri(n1, n2, n3))
else:
    print('As medidas informadas NÃO FORMAM Triângulo')



