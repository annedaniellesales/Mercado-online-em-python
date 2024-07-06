from Interfaces import Funcionario
from typing import Type

Lista_funcionarios = [] #Declarando lista de funcionários vazia
class Funcionario(Funcionario):
    """""
Classe responsável pelo gerenciamento de funcionários do Mercado
    """
    def __init__(self, nome:str) -> None:
    #Método construtor que inicializar um novo Funcionário
        self._nome = nome
        self._id = id
    
    def AdicionarFuncionario(func:Type[Funcionario])-> None:
    #Método responsável por inserir um novo funcionário no sistema.
    #Tratamento de erro 1 - Método que verifica se o funcionário existe no sistema  
         if func in Lista_funcionarios:
            print("Funcionário já admitido, não foi possível adicionar Funcionário")
         else:
             Lista_funcionarios.append(func)
             print("Funcionário admitido no sistema")
    
    def AlterarDados(func:Type[Funcionario]) -> None:
    #Método responsável por alterar dados de um Funcionário existente.
    #Tratamento de erro 2 - Método que verifica se o funcionário existe no sistema
        if func in Lista_funcionarios:
           novo_nome = input("Digite o novo nome:")
           func._nome = novo_nome
           print("Dados alterados com sucesso")
        else:
            print("Cliente não cadastrado. Tente novamente.")