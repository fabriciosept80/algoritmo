#4 - Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

print('*'*80)
print("SALÁRIO".center(80))
salario = float(input("Salário atual em R$ : "))
aumento = float(input("Entre em % o valor do aumento: "))
n_salario = salario + ((aumento / 100) * salario)
print((f'Com aumento de {aumento:.2f}% o salário de R$ {salario:.2f} vai para R$ {n_salario:.2f}.'))

