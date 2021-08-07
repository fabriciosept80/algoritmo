# 8 - Faça agora o contrário, de Fahrenheit para Celsius

print('*'*80)
print("Fahrenheit para Celsius".center(80))
temp_f = float(input("Entre com a temperatura em Fahrenheit: "))
celsius = (temp_f - 32) / 1.8
print(f"A temperatura de {temp_f}ºF convertida, fica em {celsius}ºC")