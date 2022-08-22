from dataclasses import dataclass, field
from typing import Type

from ..vos import Nome

@dataclass(repr=True, eq=True, order=True)
class Cliente():
    __nome: Nome = field(init=False, repr=True, compare=True)
    __sobrenome: str = field(init=False, repr=True, compare=True)
    __cpf: str = field(init=False, repr=True, compare=True)
    
    def __init__(self,construtor:Type['Construtor']) -> None:
        self.__nome = construtor._nome
        self.__sobrenome = construtor._sobrenome
        self.__cpf = construtor._cpf
    
    @classmethod
    def construtor(cls) -> 'Construtor':
        return cls.Construtor()

    @property
    def nome(self,) -> str:
        return self.__nome

    @property
    def sobrenome(self,) -> str:
        return self.__sobrenome

    @property
    def cpf(self,) -> str:
        return self.__cpf
    
    class Construtor():
        
        def __init__(self) -> None:
            self._nome = None
            self._sobrenome = None
            self._cpf = None
        
        def nome(self,nome:Nome):
            self._nome = nome
            return self
        
        def sobrenome(self,sobrenome:str):
            self._sobrenome = sobrenome
            return self
        
        def cpf(self,cpf:str):
            self._cpf = cpf
            return self
        
        def criar(self) -> 'Cliente':
            return Cliente(self)
