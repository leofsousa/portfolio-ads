import time
from datetime import datetime

produtos = {}

def cadastrar_produto(): #função de cadastramento de produtos.
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    localizacao = input("Digite em qual parte do deposito o produto foi armazenado: ")

    produtos[codigo] = {
        "nome" : nome,
        "preco" : preco,
        "quantidade" : quantidade,
        "localizacao" : localizacao
    }
    print('Cadastrando produto, aguarde!')
    time.sleep(1)
    print('Produto Cadastrado com sucesso!')
    return codigo

def demonstrar_produtos(): #função de desmontrar lista de produtos
    if not produtos: 
        print("Nenhum produto cadastrado!")
        return
    for codigo, dados in produtos.items():  
        quantidade = produtos[codigo]['quantidade']
        print("-" * 40)
        print(f'\nCódigo: {codigo}')
        print(f'Nome: {dados['nome']}')
        print(f'Preço: {dados['preco']}')
        print(f'Quantidade: {dados['quantidade']}')
        print(f'Localização: {dados['localizacao']}')
        if quantidade < 5:
            print('Estoque baixo! Menos de 5 itens.')
        print("-" * 40)



def alterar_quantidade():
    codigo = input("Digite o código do produto que deseja alterar a quantidade: ")
    if codigo in produtos:
        nova_quantidade = int(input('Digite a nova quantidade: '))
        produtos[codigo]["quantidade"] = nova_quantidade
        print('Quantidade atualizada com sucesso!')
    else:
        print('Produto não encontrado!')


def rastrear_produto():
    codigo = input("Digite o código do produto que deseja rastrear: ")
    if codigo in produtos:
        print(f'A localização informada do objeto é: {produtos[codigo]["localizacao"]}')
    else:
        print('Produto não encontrado!')

def remover_produto():
    codigo = input("Digite o código do produto que deseja remover: ")
    if codigo in produtos:
        print('Removendo produto, aguarde!')
        time.sleep(1)
        del produtos[codigo]
        print('Produto Removido com Sucesso!')
    else:
        print('Produto não encontrado.')

movimentacoes = []


def registrar_movimentação(tipo, codigo, descricao):
    data_hora = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    movimentacao = {
        "tipo": tipo,
        "codigo": codigo,
        "descricao": descricao,
        "data_hora": data_hora
    }
    movimentacoes.append(movimentacao)

def ver_movimentacao():
    print("Histórico de Movimentações:")
    for movimentacao in movimentacoes:
        print("-" * 40)
        print(f"Tipo:        {movimentacao['tipo']}")
        print(f"Código:      {movimentacao['codigo']}")
        print(f"Descrição:   {movimentacao['descricao']}")
        print(f"Data e Hora: {movimentacao['data_hora']}")
        print("-" * 40)


print('Bem vindo ao sistemas de gerenciamento de estoque!')
while True: # Menu de escolhas para o usuário
    print('1. Cadastrar Produto.')
    print('2. Visualizar Produtos Cadastrados.')
    print('3. Alterar quantidade de produto cadastrado.')
    print('4. Rastrear pronto dentro do depósito.')
    print('5. Remover Produto.')
    print('6. Ver movimentações')
    print('7. Sair')

    escolha = input('Escolha uma opção: ')
               
    if escolha == '1':
        print("Cadastramento de produtos iniciado!!")
        cod = cadastrar_produto()
        registrar_movimentação("Adição", cod , 'Adicionou o produto' )
        
    elif escolha == '2':
        demonstrar_produtos()
        cod = 0
        registrar_movimentação("Solicitação", cod ,'Solicitou a Lista de Produtos' )

    elif escolha == '3':
        alterar_quantidade()
        cod = cadastrar_produto()
        registrar_movimentação("Alteração", cod , 'Alterou a quantidade do produto' )

    elif escolha == '4':
        rastrear_produto()
        cod = cadastrar_produto()
        registrar_movimentação("Rastreamento", cod , f'Rastreou o produto de código: {cod}')

    elif escolha == '5':
        remover_produto()
        cod = cadastrar_produto()
        registrar_movimentação("Remoção", cod , 'Removeu o produto' )

    elif escolha == '6':
        ver_movimentacao()

    elif escolha == '7':
        print('Saindo do Sistema!')
        print('Obrigado por utilizar!')
        break
    else:
        print("Opção inválida, tente novamente!")
