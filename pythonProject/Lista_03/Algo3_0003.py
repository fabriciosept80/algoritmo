#3 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento
# e 3%  e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que
# calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população
# do país B, mantidas as taxas de crescimento.

popA = 80000
popB = 200000
txA = 0.03
txB = 0.015
count = 0
print('*'*30)
print('PROGRESSÃO'.center(30))
while popA < popB:
    popA= popA + (popA * txA)
    popB = popB + (popB * txB)
    count += 1
print(f'A população A passará a B em {count} anos!')
