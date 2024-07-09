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
    @abstractmethod
    def ExcluirFunc(self):
        pass
