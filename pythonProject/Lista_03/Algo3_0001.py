# 1 Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.

print('*'*30)
print('Notas Validas'.center(30))
n = float(input('Digite uma nota entre 0 e 10 : '))
while 0 > n or n > 10:
    n = float(input('Valor invalido, digite novamente um valor entre 0 e 10 : '))
print(f'Valor {n} válido !! Fim do programa !')
