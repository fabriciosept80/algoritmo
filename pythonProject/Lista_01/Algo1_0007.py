# 7 - Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
print('*'*80)
print("Celsius para Fahrenheit".center(80))
temp_c = float(input("Entre com a temperatura em Celsius: "))
fahrenheit = ((9 * temp_c) / 5) + 32
print(f"A temperatura de {temp_c}ºC convertida, fica em {fahrenheit}ºF")