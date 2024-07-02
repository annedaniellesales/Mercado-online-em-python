from abc import ABC, abstractmethod

class Cliente(ABC):

    @abstractmethod
    def AdicionarCliente(self):
        pass
    @abstractmethod
    def AlterarDados(self):
        pass