#6- Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
#esperada para a viagem.

print('*'*80)
print("TEMPO VIAGEM".center(80))
dist = float(input("Qual a distância a ser percorrida em KM: "))
vel_med = float(input("Qual a velocidade média em km/h: "))
tempo = dist / vel_med
print(f"O tempo da viagem do carro será de {tempo:.2f} horas")