# 11 -  Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
# a um milhão.

print('*'*80)
print("Elevado a um Milhao".center(80).title())
print()
pot = 2**1000000
npot = str(pot)
print(f"O número de digitos de 2 elevado a 1 X 10³*10³ é {len(npot)} dígitos. ")
