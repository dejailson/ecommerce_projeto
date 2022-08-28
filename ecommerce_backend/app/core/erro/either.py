from typing import Generic, TypeVar, Type
from abc import ABCMeta, abstractmethod
from .api_erro import ApiErro

E = TypeVar('E',bound=ApiErro)
S = TypeVar('S')


class Either(Generic[E, S]):
    __metaclass__ = ABCMeta

    @abstractmethod
    def tem_erro(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get(self) -> E | S:
        raise NotImplementedError()

    def foi_concluido(self) -> bool:
        return not self.tem_erro()

    @staticmethod
    def erro(valor: Type[E]) -> 'Either[E,S]':
        return Erro(valor)

    @staticmethod
    def sucesso(valor: Type[S]) -> 'Either[E,S]':
        return Sucesso(valor)
 
class Sucesso(Either):
    __valor: Type[S]

    def __init__(self, valor: Type[S]):
        self.__valor = valor

    def tem_erro(self) -> bool:
        return False

    def get(self) -> E | S:
        return self.__valor

class Erro(Either):

    __valor: Type[E]

    def __init__(self, valor: Type[E]):
        self.__valor = valor

    def tem_erro(self) -> bool:
        return True

    def get(self) -> E | S:
        return self.__valor
