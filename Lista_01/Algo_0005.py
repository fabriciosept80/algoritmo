# 5 -  Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
# preço a pagar.
print('*'*80)
print("DESCONTO".center(80))
preco = float(input("Digite o valor da mercadoria em R$: "))
desconto = float(input("Digite o valor do desconto em %: "))
paga = preco - ((desconto/100) * preco)
print(f'O valor a ser pago na mercadoria com desconto de {desconto:.2f}% será de : R$ {paga:.2f}')