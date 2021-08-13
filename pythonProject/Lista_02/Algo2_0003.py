# . João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
# seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
# faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na
# variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
# variáveis com o conteúdo ZERO.

print('*'*40)
print('PESCODROMO'.center(35))
print()
n_fish = float(input("Quantos quilos de peixe foram pescados : "))
ex_fish = n_fish - 50
if ex_fish > 0:
    multa = ex_fish * 4
else:
    multa = 0
    ex_fish = 0
print(f'Foram pescados {n_fish:.2f} kg de peixe' )
print(f'O excesso de peixe foi de {ex_fish:.2f} kg')
print(f'A multa por excesso foi de R$ {multa:.2f}')
