from abc import ABC, abstractmethod

class Cliente(ABC):
#Interface da classe cliente
    @abstractmethod
    def ValidarCliente(self):
        pass
