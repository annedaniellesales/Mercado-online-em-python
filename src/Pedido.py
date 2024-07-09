from Estoque import Estoque
from Estoque import lista_produtos
from Produto import Produto
from Cliente import Cliente
from typing import Type

sacola = [] #Lista vazia (carrinho)
class Pedido(Estoque):
    print("Você está na aba de Pedido")
    filtro = str(input("Digite o tipo de produto que voce deseja:"))
    Estoque.FiltroTipoProduto(filtro)
    marca = input("Digite a marca que você deseja:")
    quantidade = input("Digite a quantidade:")

    