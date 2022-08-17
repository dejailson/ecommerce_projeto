from dataclasses import dataclass
from typing import Type


@dataclass(repr=True, eq=True, order=True)
class Cliente():
    __nome: str
    __sobrenome: str
    __cpf: str

    @property
    def nome(self,) -> str:
        return self.__nome

    @property
    def sobrenome(self,) -> str:
        return self.__sobrenome

    @property
    def cpf(self,) -> str:
        return self.__cpf
