#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
print('*'*30)
print('Usuário e Senha'.center(30))
nome = input("Digite o nome do usuário: ")
pwd = input("Digite a sua senha: ")
while nome == pwd:
    print("\033[7;33mUsuário e senha NÃO podem ser iguais. Digite novamente abaixo.\033[m")
    nome = input("Digite o nome do usuário: ")
    pwd = input("Digite a sua senha: ")
print('#'*30)
print("Sistema online".center(30))