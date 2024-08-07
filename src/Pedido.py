from Estoque import Estoque
from Estoque import lista_produtos
from typing import Type
import time

Carrinho = [] #Lista de compras vazias

class Pedido(Estoque):
    """
 Classe responsável por realizar o pedido do cliente
 """
    def FazerPedido():
        print("Olá, você está na aba de Pedidos:\n")
        #Método responsável por inserir um produto no carrinho
        filtro = str(input("Qual tipo de produto você deseja?:"))
        produtos_filtrados = [produto for produto in lista_produtos if produto._tipo == filtro]  #Filtra os produtos que existem no estoque
        if produtos_filtrados:
            for produto in produtos_filtrados:
                print(f"{produto._marca}, {round(produto._preco,2)}")
        marca = str(input(f"Das marcas listadas de {produto._tipo}, qual voce deseja?")) #Filtra os produtos que existem no estoque
        produtos_filtrados = [produto for produto in lista_produtos if produto._marca == marca]
        if produtos_filtrados:
            for produto in produtos_filtrados:
                print("Produto selecionado:\n")
                print(f"{produto._tipo} |{produto._marca} |R${produto._preco}und")
                print("\n")
                produto._qtd = int(input(f"Digite a quantidade de {produto._tipo} da {produto._marca} você deseja:"))
                produto._preco *= produto._qtd #Calculando o preço total de acordo com a quantidade
                Carrinho.append(produto) #Insere o produto desejado na lista Carrinho
                print("Produto adicionado no carrinho com sucesso!\n")


    def ExibirCarrinho():
    #Exibe todos os items que estão no carrinho
        for produto in Carrinho:
            print("Os produtos do seu carrinho são:\n")
            print(f"{produto._tipo}| {produto._marca}| {produto._peso} kg| R${round(produto._preco,2)}| {produto._qtd} und")

    def EditarCarrinho():
    #Método responsável por excluir ou editar quantidade de produtos da lista Carrinho
        escolha = int(input("Digite a opção desejada:\n1- Excluir o produto do Carrinho de compras\n2- Editar a quant. de items de cada produto\n"))
        #1 - excluir o item e todas suas quantidades do carrinho
        if escolha == 1:
            excluir_tipo = str(input("Digite o tipo de produto do seu carrinho que quer editar:"))
            produtos_filtrados = [produto for produto in Carrinho if produto._tipo == excluir_tipo]
            if produtos_filtrados:
                for produto in produtos_filtrados:
                    print(f"Esses são as marcas de {excluir_tipo} que estão no carrinho:")
                    print(f"{produto._marca}| {round(produto._preco,2)}")
            excluir_marca = str(input(f"Digite a marca de {excluir_tipo} que deseja excluir:"))
            produtos_filtrados = [produto for produto in Carrinho if produto._marca == excluir_marca]
            if produtos_filtrados:
                for produto in Carrinho:
                    Carrinho.remove(produto)
            print("Produto excluido com sucesso!")

        #2 - Editar a quantidade existente de um item no carrinho
        elif escolha == 2:
            for produto in Carrinho:
                editar_tipo = str(input("Digite o tipo de produto que quer editar:"))
                produtos_filtrados = [produto for produto in Carrinho if produto._tipo == editar_tipo]
                if produtos_filtrados:
                    for produto in produtos_filtrados:
                         print(f"Esses são as marcas de {editar_tipo} que estão no carrinho:")
                         print(f"{produto._marca} |{round(produto._preco,2)}| {produto._qtd} und")
                editar_marca = str(input(f"Que marca de {editar_tipo} você quer editar a quant.?"))
                produto._preco = produto._preco/produto._qtd
                produtos_filtrados = [produto for produto in Carrinho if produto._marca == editar_marca]
                produto._qtd = int(input("Qual a nova quantidade?"))
                if produtos_filtrados:
                    for produto in Carrinho:
                        produto._preco *= produto._qtd
                        print(f"{produto._marca}| {round(produto._preco,2)} | {produto._qtd}")
                print("Quantidade de items alterado com sucesso!")
    
    def FinalizarCompra():
    #Escolhe o método de pagamento e finaliza a compra
         valor_compra = 0
         for produto in Carrinho:
            print(f"{produto._tipo}| {produto._marca}| {produto._peso} kg| R${round(produto._preco,2)}|{produto._qtd} und")
            valor_compra += produto._preco
         print('\n')
         forma_pagamento = input(f"O Valor da sua compra foi R${round(valor_compra,3)}\nQual forma de pagamento?\n1-Vale Alimentação\n2-Cartão crédito ou debito\n3-Pix")
         entrega = str(input("Deseja o serviço de entrega gratuito?"))
         print("Processamento pagamento...")
         time.sleep(2)
         print("\nPagamento realizado com sucesso!\nRetire seus recebidos\nObrigado,volte sempre!")

    