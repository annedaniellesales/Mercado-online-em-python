from Interfaces import Produto
import uuid
import sys

Lista_produtos = [] #Adicionando uma lista vazia de produtos
class Produto(Produto):
    #Implementação da classe produto com seus atributos privados
    def __init__(self,tipo:str, marca:str, preco:float, qtd:int) -> None:
        self._tipo = tipo
        self._marca = marca
        self._preco = preco
        self._qtd = qtd
        self._id = uuid.uuid4()
    
    def AdicionarProduto(cls, tipo, marca, preco, qtd) -> None:
    #Teste de verificação se o produto esta na lista
        if self._id in Lista_produtos:
            print("Produto já cadastrado")
        else:
            Lista_produtos.append()
            print("Produto cadastrado com sucesso!")

    def AlterarDadosProduto(self):
        return super().AlterarDadosProduto()

Arroz = Produto('arroz','camil', 7.82, 1200)
Arroz.AdicionarProduto()
Arroz.AdicionarProduto()