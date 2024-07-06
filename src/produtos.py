from Interfaces import Produto
from typing import Type

Lista_produtos = [] #Adicionando uma lista vazia de produtos
class Produto(Produto):
    """""
Classe responsável pelo gerenciamento de produtos do mercado
    """
    def __init__(self,tipo:str, marca:str, preco:float, qtd:int) -> None:
    #Método construtor que inicializa um novo produto na lista de produtos
        self._tipo = tipo
        self._marca = marca
        self._preco = preco
        self._qtd = qtd
    
    def AdicionarProduto(produto:Type[Produto]) -> None:
    #Método responsável por cadastrar um novo produto no sistema
    #Tratamento de erro 1 - Verifica se o produto ja existe no sistema
         if produto in Lista_produtos:
            print("Produto já cadastrado no sistema, não foi possível cadastrar novamente!")
         else:
             Lista_produtos.append(produto)
             print("Novo produto cadastrado com sucesso!")
    
    