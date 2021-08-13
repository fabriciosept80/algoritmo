#3- Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
# o total em segundos.
print('*'*80)
print("SEGUNDOS".center(80))
dias = int(input("Entre com a quantidade de dias: "))
horas = int(input("Entre com a quantidade de horas: "))
minutos = int(input("Entre com a quantidade de minutos: "))
segundos = int(input("Entre com a quantidade segundos: "))

diass = ((dias * 24) * 3600)
horass = horas * 3600
minutoss = minutos * 60
segundoss = diass + horass + minutoss + segundos
print(f"O total de segundos em {dias} dias,{horas} horas,{minutos} minutos e {segundos} segundos é : {segundoss} segundos")