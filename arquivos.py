# 1 - importação de pacotes

import json
import pytest

# 2 - Classe

# 3 - Definições (Funções e métodos)

dados = {}

dados['cliente'] = [] # indica a criação de um vetor, matriz, lista...
dados['cliente'].append({
    'nome':'Juca',
    'telefone':'11999999999',
    'email': 'juca@iterasys.com.br'
})
dados['cliente'].append({
    'nome':'Ana',
    'telefone':'21888888888',
    'email': 'ana@iterasys.com.br'
})

def criar_json():
    with open('clientes.json', 'w') as outfile:
        json.dump(dados, outfile, indent=4)

def ler_json():
    with open('clientes2.json', 'r', encoding='utf8') as outfile:
        return json.load(outfile)

def testar_criar_json():
    criar_json()
    print(dados['cliente'])

def testar_ler_json():
    print(ler_json())
