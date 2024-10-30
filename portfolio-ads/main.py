import time
import datetime

produtos = {}

def cadastrar_produto(): #função de cadastramento de produtos.
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = input("Digite a quantidade do produto: ")
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

def demonstrar_produtos(): #função de desmontrar lista de produtos
    if not produtos: 
        print("Nenhum produto cadastrado!")
        return
    for codigo, dados in produtos.items():  
        quantidade = produtos[codigo]['quantidade']
        print(f'\nCódigo: {codigo}')
        print(f'Nome: {dados['nome']}')
        print(f'Preço: {dados['preco']}')
        print(f'Quantidade: {dados['quantidade']}')
        print(f'Localização: {dados['localizacao']}')
        if quantidade < '5':
            print('Estoque baixo! Menos de 5 itens.')



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
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    movimentacao = {
        "tipo": tipo,
        "codigo": codigo,
        "descricao": descricao,
        "data_hora": data_hora
    }
    movimentacoes.append(movimentacao)

print('Bem vindo ao sistemas de gerenciamento de estoque!')
while True: # Menu de escolhas para o usuário
    print('1. Cadastrar Produto.')
    print('2. Visualizar Produtos Cadastrados.')
    print('3. Alterar quantidade de produto cadastrado.')
    print('4. Rastrear pronto dentro do depósito.')
    print('5. Remover Produto.')
    print('6. Sair')

    escolha = input('Escolha uma opção: ')
               
    if escolha == '1':
        print("Cadastramento de produtos iniciado!!")
        cadastrar_produto()
        
    elif escolha == '2':
        demonstrar_produtos()
        
    elif escolha == '3':
        alterar_quantidade()

    elif escolha == '4':
        rastrear_produto()

    elif escolha == '5':
        remover_produto()

    elif escolha == '6':
        print('Saindo do Sistema!')
        print('Obrigado por utilizar!')
        break
    else:
        print("Opção inválida, tente novamente!")
