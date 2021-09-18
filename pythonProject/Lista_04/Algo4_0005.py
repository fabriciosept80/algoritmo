#5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de
# 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.
result = []
a = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we  are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
b = "python"
print('*'*40)
print("PHYTON IN PHRASE".center(40))
print()
a = a.replace(","," ")
a = a.replace(":"," ")
a = a.replace("."," ").lower().split()

for t in a:
    for x in b:
        if x in t and len(t) > 4 and t not in result:
            result.append(t)
print(f'Segue lista de palavras com mais de 4 caracteres e com letras PYTHON em seu conteúdo.')
print('',*result,sep='\n\033[1;34m-\033[m')
print('-'*40)
print(f'Total de palavras : \033[1;34m{len(result)}\033[m')


