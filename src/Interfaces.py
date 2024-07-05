from abc import ABC, abstractmethod

class Cliente(ABC):
#Interface da classe cliente
    @abstractmethod
    def AdicionarCliente(self):
        pass
    @abstractmethod
    def AlterarDados(self):
        pass

class Funcionario(ABC):
#Interface da classe funcionario
    @abstractmethod
    def AdicionarFuncionario(self):
        pass
    @abstractmethod
    def AlterarDados(self):
        pass

class Produto(ABC):
#Interface da classe produto
    @abstractmethod
    def AdicionarProduto(self):
        pass
    @abstractmethod
    def AlterarDadosProduto(self):
        pass
    def ExcluirProduto(self):
        pass