# 1 - imports / bibliotecas

# 2 - Classes

# 3 - Métodos e Funções
# def = definition = definição

def print_hi(name):
    print(f'Oi, {name}') # A partir do Python 3
    print('Oi, ' + name) # Antes do Python 3

def calcular_area_do_retangulo(largura, comprimento):
    return largura  * comprimento

def calcular_area_do_quadrado(lado):
    return lado * lado

def calcular_area_do_triangulo(largura, comprimento):
    return (largura * comprimento) / 2

def contagem_progressiva(fim):
    for numero in range(fim): # repetir o bloco de zero até o fim
        print(numero) # exibir o número

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        contador = numero + 1
        print(f'{contador} - {nome}')

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>9}'.format(numero))

# Estrutura de identificação / execução do script
if __name__ == '__main__':
    print_hi('Pedro Junio')

# Chamar função de cálculo de área do retângulo
resultado = calcular_area_do_retangulo(3,4)
print(f'A área do retângulo é de {resultado} metros quadrados')

# Chamar função de cálculo de área do quadrado
resultado = calcular_area_do_quadrado(5)
print(f'A área do quadrado é de {resultado} metros quadrados')

# Chamar função de cálculo de área do triangulo
resultado = calcular_area_do_retangulo(6,7)
print(f'A área do triangulo é de {resultado} metros quadrados')

# Executar uma contagem progressiva
contagem_progressiva(10)

# Exibir o nome do candidato várias vezes
apoiar_candidato('Faker', 10)

# Brincar de plim
brincar_de_plim(100)
