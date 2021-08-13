# 10 -  Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias.

print('*'*80)
print("redução do tempo de vida".center(80).title())
print()
cigar_day = int(input("Qual a quantidade de cigarros fumados por dia: "))
cigar_years = int(input("Quantos anos você fumou ou fuma: "))
lost_life = ((((cigar_years * 365) * (cigar_day * 10)) / 60) / 24)
print(f"O cidadão já perdeu {lost_life:.2f} dias da vida dele")