from Produto import Produto
from typing import Type
from datetime import date

lista_produtos = [] #Lista vazia de produtos
class Estoque(Produto):
    """"
Classe responsável por gerenciar quantidades de produtos do Mercado
    """
    def AdicionarProduto() -> None:
    #Método responsável por cadastrar um novo produto no sistema
     filtro = str(input("Digite o tipo de produto que deseja cadastrar no estoque:"))
     produtos_filtrados = [produto for produto in lista_produtos if produto._tipo == filtro]  #Filtra os produtos que existem no estoque
     if produtos_filtrados:
        for produto in produtos_filtrados:
                print(f"{produto._marca}, {produto._preco}")
        op = str(input(f"Das marcas listadas de {produto._tipo},deseja cadastrar uma diferente?")) #Filtra os produtos que existem no estoque
        if op == 'sim':
            print("Aba de adição de estoque")
            marca = str(input(f"Qual a marca de {filtro}?"))
            preco = str(input(f"Qual preço unitário de {filtro}?"))
            qtd = str(input(f"Quantidade em estoque?"))
            peso = str(input(f"Peso unitário?"))
            novo_produto = Produto(filtro,marca,preco,qtd,peso)
            lista_produtos.append(novo_produto)
            print("Produto inserido no estoque.")
        if op == 'nao':
            print("Então ta bom.")
     else:
        marca = str(input(f"Qual a marca de {filtro}?"))
        preco = str(input(f"Qual preço unitário de {filtro}?"))
        qtd = str(input(f"Quantidade em estoque?"))
        peso = str(input(f"Peso unitário?"))
        novo_produto = Produto(filtro,marca,preco,qtd,peso)
        lista_produtos.append(novo_produto)
        print("Produto inserido no estoque.")

    def ExcluirProduto() -> None:
    #Excluir um produto do sistema e todas suas quantidades
      filtro = str(input("Digite o tipo de produto que deseja excluir do sistema"))
      produtos_filtrados = [produto for produto in lista_produtos if produto._tipo == filtro]  #Filtra os produtos que existem no estoque
      if produtos_filtrados:
        for produto in produtos_filtrados:
                print(f"{produto._marca}, {produto._preco}")
        confirmacao = str(input(f"Você tem certeza que deseja excluir {produto._qtd} und de {produto._tipo}?")) #Filtra os produtos que existem no estoque
        if confirmacao == 'sim':
            lista_produtos.remove(produto)
            print("Produtos com todas as unidades excluidos com sucesso!\n")
    
    def ListarEstoque() -> None:
        print("Hoje", date.today(), "O estoque do mercado é:")
        for produto in lista_produtos:
            print(f"{produto._tipo} | {produto._marca} | {produto._qtd} und | R${produto._preco} unt | {produto._peso * produto._qtd}kg | R${produto._preco * produto._qtd} totais")

    def ValorEstoque() -> None:
        valor = 0
        peso = 0
        for produto in lista_produtos:
            valor += (produto._preco * produto._qtd)
            peso += (produto._peso * produto._qtd)
        print(f"O valor de {peso}kg de produtos totais é R${valor}")
    
    def FiltroTipoProduto() -> None:
        filtro = str(input("Digite o tipo que deseja filtrar:"))
        produtos_filtrados = [produto for produto in lista_produtos if produto._tipo == filtro]
        if produtos_filtrados:
            for produto in produtos_filtrados:
                print(f"{produto._marca} | R$ {produto._preco* produto._qtd} | {produto._qtd} und | {produto._peso * produto._qtd} kg")
        else:
            print("Produto não disponível. Tente novamente.")

    
    arroz = Produto('arroz', 'camil', 7.85,100,1)
    calda_morango = Produto('calda de morango', 'heisn', 9.85,50,0.50)
    feijao= Produto('feijao', 'joao', 6.85,500,1)
    lista_produtos.append(arroz)
    lista_produtos.append(calda_morango)
    lista_produtos.append(feijao)
