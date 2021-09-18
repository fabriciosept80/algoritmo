#4. Seja o statement sobre diversidade: “The Python Software Foundation and the global Python community welcome and
# encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we
# are working to help each other live up to these principles. We want our community to be more diverse: whoever you are,
# and whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com split(), a seguir crie uma
# lista com as palavras que começam ou terminam com uma das letras “python”. Imprima a lista resultante. Não se esqueça
# de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.
count=0
começam = list()
terminam = list()
resultante = list()
a = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we  are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
b = "python"

a = a.replace(","," ")
a = a.replace(":"," ")
a = a.replace("."," ").lower().split()

while count < len(a):
    if (a[count][0]) in b:
        começam.append(a[count][0])
    if (a[count][-1]) in b:
        terminam.append(a[count][-1])
    count += 1
resultante.extend(começam)
resultante.extend(terminam)
print('#'*45)
print('RESPOSTAS'.center(45))
print()
print(f'1- Gere uma lista de palavras deste texto com split() : {a}')
print(f'2- Lista com as palavras que começam com "phyton" : {começam}')
print(f'3- Lista com as palavras que terminam com "phyton" : {terminam}')
print(f'4- Lista resultante : {resultante}')





