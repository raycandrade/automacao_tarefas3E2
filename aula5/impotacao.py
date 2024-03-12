'''
Para utilizarmos as funcoes criadas em outros
arquivos de codigo fonte devemos importa-las. Para 
isso utilizamos o comando import ou from import

Exeemplo 1: Importar todas as funcoes do arquivo
funcoes
'''
import funcoes

base = float(input('Digite a base do triangulo:'))
altura = float(input('Digite a altura do triangulo:'))

area = funcoes.calcularAreaTriangulo(base,altura)
altura = 