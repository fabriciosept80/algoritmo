# Determine se um ano é bissexto. Verifique no Google como fazer isso...
print('#'*40)
print('Ano Bissexto'.center(40))
ano = int(input("Entre com o ano: "))
if ano % 4 == 0 or (ano % 400 == 0 and ano % 100 != 0):
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')