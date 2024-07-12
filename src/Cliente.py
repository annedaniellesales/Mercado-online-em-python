from typing import Type
from Interfaces import Cliente

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

    def ValidarCliente() -> None:
    #Método responsável por validar um cliente existente
        validando_CPF = str(input("Se identifique, digite seu CPF:"))
        clientes_filtrados = [cliente for cliente in Lista_clientes if cliente._CPF == validando_CPF]
        if clientes_filtrados:
            for cliente in clientes_filtrados:
                print(f"Bem vindo {cliente._nome}, prossiga com suas compras.")
        else:
            print("Cliente não cadastrado")
            nome = str(input("Digite seu nome completo:"))
            endereco = str(input("Digite seu endereco:"))
            novo_cliente = Cliente(nome,validando_CPF, endereco)
            print("Cliente cadastrado com sucesso! Prossiga com suas compras.")
        return cliente
    
ana = Cliente('ana', '70261392662', 'Rua arlindo')
Lista_clientes.append(ana)
joao = Cliente('joao', '70261392662', 'Rua arlindo')
Lista_clientes.append(joao)