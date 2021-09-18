#Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também divisíveis por 7?
#Resposta: 183
print("#"*30)
print('List Comprehension'.center(30))
print()
print('Total de números pares e divisíveis por 7:',len([x for x in range(1067,3628) if x % 2 == 0 and x % 7 == 0]))