
from typing import Type

class Produto():
    """""
Classe responsável criação de produtos no mercado
    """
    def __init__(self,tipo:str, marca:str, preco:float, qtd:int) -> None:
    #Método construtor que inicializa um novo produto na lista de produtos
        self._tipo = tipo
        self._marca = marca
        self._preco = preco
        self._qtd = qtd


        

    