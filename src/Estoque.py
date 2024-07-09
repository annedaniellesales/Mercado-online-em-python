from Produto import Produto
from typing import Type
from datetime import date

lista_produtos = [] #Lista vazia de produtos
class Estoque(Produto):
    """"
Classe responsável por gerenciar quantidades de produtos do Mercado
    """
    def AdicionarProduto(produto:Type[Produto]) -> None:
    #Método responsável por cadastrar um novo produto no sistema
    #Tratamento de erro 1 - Verifica se o produto ja existe no sistema
         if produto in lista_produtos:
            print("Produto já cadastrado no sistema, não foi possível cadastrar novamente!")
         else:
             lista_produtos.append(produto)
             print("Novo produto cadastrado com sucesso!")
    
    def ExcluirProduto(produto:Type[Produto]) -> None:
    #Excluir um produto do sistema
        if produto in lista_produtos:
            lista_produtos.pop(produto)
        else:
            print("Produto não cadastrado no sistema. Não foi possível concluir a ação!")

    def ListarEstoque() -> None:
        print("Hoje", date.today(), "O estoque do mercado é:")
        for produto in lista_produtos:
            print(f"{produto._tipo}, {produto._marca}: {produto._qtd} und")

    def Valor_Estoque() -> None:
        valor = 0
        for produto in lista_produtos:
            valor += (produto._preco * produto._qtd)
        print(valor)
    
    def FiltroTipoProduto(filtro) -> None:
        produtos_filtrados = [produto for produto in lista_produtos if produto._tipo == filtro]
        if produtos_filtrados:
            for produto in produtos_filtrados:
                print(f"{produto._marca}, {produto._preco}")
        else:
            print("Produto não disponível. Tente novamente.")
    
    arroz = Produto('arroz',' camil', 7.82,100)
    AdicionarProduto(arroz)
    feijao = Produto('feijao', 'seu joao', 7.12,100)
    AdicionarProduto(feijao)
    
    FiltroTipoProduto('arroz')



