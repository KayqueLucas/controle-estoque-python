# === Sistema de Controle de Estoque com Python ===
# Este sistema permite adicionar, atualizar, excluir e visualizar produtos de uma loja de eletrônicos.

# Dicionário que armazena os produtos do estoque
estoque = {}

# Função para exibir o menu principal
def mostrar_menu():
    print("\n=== SISTEMA DE ESTOQUE ===")
    print("1 - Adicionar Produto")
    print("2 - Atualizar Produto")
    print("3 - Excluir Produto")
    print("4 - Visualizar Estoque")
    print("5 - Sair")

# Função para adicionar um novo produto ao estoque
def adicionar_produto():
    nome = input("Nome do produto: ").title()
    if nome in estoque:
        print("Produto já existe no estoque.")
    else:
        try:
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade: "))
            estoque[nome] = {"preco": preco, "quantidade": quantidade}
            print("Produto adicionado com sucesso.")
        except ValueError:
            print("Erro: preço e quantidade devem ser numéricos.")

# Função para atualizar um produto existente
def atualizar_produto():
    nome = input("Nome do produto a atualizar: ").title()
    if nome in estoque:
        try:
            preco = float(input("Novo preço: "))
            quantidade = int(input("Nova quantidade: "))
            estoque[nome]["preco"] = preco
            estoque[nome]["quantidade"] = quantidade
            print("Produto atualizado.")
        except ValueError:
            print("Erro: preço e quantidade devem ser numéricos.")
    else:
        print("Produto não encontrado.")

# Função para excluir um produto do estoque
def excluir_produto():
    nome = input("Nome do produto a excluir: ").title()
    if nome in estoque:
        del estoque[nome]
        print("Produto excluído.")
    else:
        print("Produto não encontrado.")

# Função para exibir todos os produtos do estoque
def visualizar_estoque():
    if estoque:
        print("\n=== ESTOQUE ATUAL ===")
        for nome, dados in estoque.items():
            print(f"{nome}: R$ {dados['preco']:.2f}, Quantidade: {dados['quantidade']}")
    else:
        print("Estoque vazio.")

# Loop principal do sistema
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        atualizar_produto()
    elif opcao == "3":
        excluir_produto()
    elif opcao == "4":
        visualizar_estoque()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
