from Produto import Produto
from Produto import Lista_produtos
from typing import Type

class Mercado(Produto):
    """""
Classe responsável pela vendas no mercado
    """""

    def FazerCompra(produto:Type[Produto]) -> None:
        for produto in Lista_produtos:
            print(produto._tipo)