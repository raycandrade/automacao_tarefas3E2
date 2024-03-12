'''
As funções são utilizadas para modularizar o código, ou seja,
dividi-lo em partes menores, que podem ser reutilizadas.

Estrutura:

def nome_funcao(param1, param2):
    faz algo
    return valor

Exemplos:
'''

#funcao 1
def calculadorAreaTriangulo(base,altura):
    area = (base * altura) / 2
    return area

def login(usuario, senha):
    if usuario == 'admin' and senha = '123':
        return True
    else:
        return False 
    
#chamar a função
#print(login("admin", '123'))

#area2 = calcularAreaTriangulo(100,50)
#print('A area do triangulo é', area2)
