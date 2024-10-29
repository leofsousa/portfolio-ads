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
    print('Produto Cadastrado com sucesso!')

    def demonstrar_produtos(): #função de desmontrar lista de produtos
        if not produtos: 
            print("Nenhum produto cadastrado!")
            return
        for codigo, dados in produtos.itens():  
            print(f'\nCódigo: {codigo}')
            print(f'Nome: {dados['nome']}')
            print(f'preco: {dados['preco']}')
            print(f'quantidade: {dados['quantidade']}')
            print(f'localizacao: {dados['localizacao']}')

print('Bem vindo ao sistemas de gerenciamento de estoque!')
while True: # Menu de escolhas para o usuário
    print('1. Cadastrar Produto.')
    print('2. Visualizar Produtos Cadastrados.')
    print('3. Remover Produto.')
    print('4. Sair')

    escolha = input('Escolha uma opção: ')
               
    if escolha == '1':
        cadastrar_produto()


    elif escolha == '4':
        print('Saindo do Sistema!')
        print('Obrigado por utilizar!')
        break
    else:
        print("Opção inválida, tente novamente!")
