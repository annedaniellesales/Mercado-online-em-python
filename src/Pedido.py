from Estoque import Estoque
from Estoque import lista_produtos
from Produto import Produto
from typing import Type

Carrinho = [] #Lista de compras vazias
qtd = None
class Pedido(Estoque):
    def FazerPedido():
        print("Você está na aba de Pedido")
        filtro = str(input("Digite o tipo de produto que voce deseja:"))
        produtos_filtrados = [produto for produto in lista_produtos if produto._tipo == filtro]
        if produtos_filtrados:
            for produto in produtos_filtrados:
                print(f"{produto._marca}, {produto._preco}")
        marca = str(input(f"Digite a marca de {produto._tipo} que voce deseja:"))
        produtos_filtrados = [produto for produto in lista_produtos if produto._marca == marca]
        if produtos_filtrados:
            for produto in produtos_filtrados:
                print(f"{produto._tipo},{produto._marca}, {produto._preco}")
                global qtd #Declarando uma variavel global
                qtd = int(input(f"Digite a quantidade de {produto._tipo}, {produto._marca}:"))
                produto._preco *=qtd
                Carrinho.append(produto)

    def ExibirCarrinho():
        for produto in Carrinho:
            print(f"{produto._tipo},{produto._marca}, {produto._preco},{qtd} und")

    def EditarCarrinho():
        escolha = int(input("Digite 1 para excluir o produto e 2 para editar a quantd. de produtos:"))
        if escolha == 1:
            excluir_tipo = str(input("Digite o tipo de produto que quer excluir:"))
            produtos_filtrados = [produto for produto in Carrinho if produto._tipo == excluir_tipo]
            if produtos_filtrados:
                for produto in produtos_filtrados:
                    print(f"{produto._marca}, {produto._preco}")
            excluir_marca = str(input("Digite a marca que deseja excluir:"))
            produtos_filtrados = [produto for produto in Carrinho if produto._marca == excluir_marca]
            if produtos_filtrados:
                for produto in Carrinho:
                    Carrinho.remove(produto)

        elif escolha == 2:
            for produto in Carrinho:
                editar_tipo = str(input("Digite o tipo de produto que quer editar:"))
                produtos_filtrados = [produto for produto in Carrinho if produto._tipo == editar_tipo]
                if produtos_filtrados:
                    for produto in produtos_filtrados:
                        print(f"{produto._marca}, {produto._preco}")
                editar_marca = str(input("Digite a marca que deseja excluir:"))
                produtos_filtrados = [produto for produto in Carrinho if produto._marca == editar_marca]
                nova_qtd = int(input("Digite a nova quantidade desejada:"))
                if produtos_filtrados:
                    for produto in Carrinho:
                         produto._qtd = nova_qtd
            
                

    FazerPedido()
    EditarCarrinho()
    ExibirCarrinho()