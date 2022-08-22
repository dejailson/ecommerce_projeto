from dataclasses import dataclass, field
from ...core.decoradores.validadores import Validador


@dataclass(frozen=True, repr=True, eq=True, order=True)
class Nome():
    __valor: str= field(default=None,init=True)

    @property
    def valor(self,) -> str:
        return self.__valor

    @Validador.nao_nulo_validador(mensagem = 'Nome não pode ser nulo.')
    @staticmethod
    def criar(nome: str = None) -> 'Nome':
        return Nome(nome)
