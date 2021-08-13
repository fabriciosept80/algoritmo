#7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
#ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
#em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
#compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas

print('*'*30)
print('aquarela'.capitalize().center(28))
print()
m2 = float(input('Quantos m² serão pintados: '))
total_tinta = round((m2 / 3 / 18) + 0.5)
print(f'Total de lata(s): {total_tinta:.0f}')
print(f'Valor total: R$ {total_tinta*80:.2f}')
