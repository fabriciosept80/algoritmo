#6-Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
#e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
#quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
#descontos e o salário líquido, conforme a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

def ir(s_total):
    return s_total * (0.11)
def inss(s_total):
    return s_total * (0.08)
def sind(s_total):
    return s_total * (0.05)
def liquido(s_total):
    return s_total - ir(s_total) - inss(s_total) - sind(s_total)
print('*'*30)
print('FOLHA DE PAGAMENTO'.center(29))
print()
s_hora = float(input('Qual o seu salário hora em R$: '))
h_trampo = float(input('Qual o total de horas trabalhadas: '))
s_total = s_hora * h_trampo
print(f'O salário bruto das {h_trampo} horas trabalhadas: R$ {s_total:.2f}.')
print(f'Desconto Imposto de Renda: R$ {ir(s_total):.2f}.')
print(f'Desconto INSS: R$ {inss(s_total):.2f}.')
print(f'Desconto Sindical: R$ {sind(s_total):.2f}.')
print(f'Valor Liquido a Receber: R$ {liquido(s_total):.2f}.')

