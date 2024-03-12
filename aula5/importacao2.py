from funcoes import login

while True:
    user = input('Digite o nome do usuario:')
    pwd = input('Digite a senha do usuario:')
    if login(user, pwd):
        break
    else:
        print('Logado com sucesso')
        break
else:
    print('Tente novamente!')