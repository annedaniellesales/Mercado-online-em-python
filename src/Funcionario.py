from typing import Type
from Estoque import Estoque
import sys

Lista_funcionarios = [] #Declarando lista de funcionários vazia
class Funcionario():
    """""
Classe responsável pelo gerenciamento de funcionários do Mercado
    """
    def __init__(self, nome:str,CPF:str,cargo:str) -> None:
    #Método construtor que inicializar um novo Funcionário
        self._nome = nome
        self._CPF = CPF
        self.cargo = cargo

    def ValidarFuncionario() -> None:
        validando_CPF = str(input("Se identifique, digite seu CPF:"))
        func_filtrados = [func for func in Lista_funcionarios if func._CPF == validando_CPF]
        if func_filtrados:
            for func in func_filtrados:
                senha = str(input("Digite a senha de funcionário para acessar o sistema:"))
                if senha == 'admin2024':
                    print(f"Bem vindo {func._nome}.")
                else:
                    print("Senha incorreta. Não foi possível fazer login!")
                    sys.exit()
        else:
            print("Funcionario não cadastrado, não foi possível concluir a ação. Entre em contato com RH!")
            sys.exit()

    def AdicionarFuncionario(self, nome, CPF, cargo)-> None:
    #Método responsável por inserir um novo funcionário no sistema.
        novo_func = Funcionario(nome,CPF,cargo)
        Lista_funcionarios.append(novo_func)
        print(f"{novo_func._nome} admitido no sistema.")
    
    def AdicionarProduto():
       Estoque.AdicionarProduto()
    def ExcluirProduto():
       Estoque.ExcluirProduto()

    def ListarEstoque():
       Estoque.ListarEstoque()

    def ValorEstoque():
       Estoque.ValorEstoque()
    def FiltroTipoProduto():
       Estoque.FiltroTipoProduto()


Matheus = Funcionario('Matheus silva', '789','gerente')
Lista_funcionarios.append(Matheus)