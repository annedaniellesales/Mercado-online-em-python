from Interfaces import Cliente
from typing import Type

Lista_clientes = [] #Criando lista vazia de clientes
class Cliente(Cliente):
    """""
Classe responsável por representar os clientes cadastrados do mercado.
    """
    def __init__(self, nome:str, CPF:str, endereco:str) -> None:
    #Construtor que inicializa um novo cliente
        self._nome = nome
        self._CPF = CPF
        self._endereco = endereco

    def AdicionarCliente(cliente:Type[Cliente]) -> None:
    #Método responsável por adicionar um cliente na lista
    #Tratamento de erro 1 - Verificar se o cliente já existe no sistema
        if cliente in Lista_clientes:
            print("Cliente já cadastrado! Tente novamente!")
        else:
            Lista_clientes.append(cliente)
            print("Usuário cadastrado com sucesso! Prossiga com suas compras.")

    def AlterarDados(cliente:Type[Cliente]) -> None:
    #Método de alterar dados de clientes já existentes na lista
    #Tratamento de erro 2 - Verificar se o cliente já existe no sistema
        if cliente in Lista_clientes:
           novo_nome = input("Digite o novo nome:")
           novo_CPF = input("Digite o novo CPF:")
           novo_endereco = input("Digite o novo endereço:")
           cliente._nome = novo_nome
           cliente._CPF = novo_CPF
           cliente._endereco = novo_endereco
           print("Dados alterados com sucesso")
        else:
            print("Cliente não cadastrado. Tente novamente.")
    