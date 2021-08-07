#9-Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

print('*'*80)
print("Carro Alugado".center(80))
print()
dias = int(input("Qual a quantidade de dias que o cliente ficou com o carro: "))
km = float(input("Quantos KM o cliente percorreu com o carro: "))
paga = (dias * 60) + (0.15 * km)
print(f"O total a pagar do cliente será de R$ {paga:.2f}.")