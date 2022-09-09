from dataclasses import dataclass, field
from typing import Union
from app.core.decoradores.validadores import Validador, Validador
from app.core.erro import Either
from app.core.decoradores.validadores.erros import NaoBrancoValidadorErro


@dataclass(frozen=True, eq=True, order=True)
class Nome():
    __valor: str= field(default=None,init=True)
    erros = Union[NaoNuloValidadorErro,NaoBrancoValidadorErro]

    @property
    def valor(self,) -> str:
        return self.__valor

    @staticmethod
    @Validador.nao_branco_validador(mensagem = 'Nome deve conter um conjunto de caracteres.')
    def criar(nome: str = None) -> Either[erros,'Nome']:
        return Either.sucesso(Nome(nome))

    def __repr__(self):
        return f'Nome({self.__valor})'
