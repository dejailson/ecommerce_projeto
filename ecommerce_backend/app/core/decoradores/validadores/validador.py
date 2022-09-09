from functools import wraps
from typing import Any
from ...erro import Either
from .erros import NaoNuloValidadorErro
from .erros import NaoBrancoValidadorErro

class Validador():
      
    @classmethod
    def nao_nulo_validador(cls,mensagem):
        def decorator(function):
            @wraps(function)
            def wrapper(valor) -> Either[NaoNuloValidadorErro,Any]:
                if valor is None:
                    return Either.erro(NaoNuloValidadorErro(mensagem))
                return function(valor)
            return wrapper
        return decorator
    
    @classmethod
    def nao_branco_validador(cls,mensagem):
        def decorator(function):
            @wraps(function)
            @Validador.nao_nulo_validador(mensagem = 'Atributo não pode ser nulo.')
            def wrapper(valor) -> Either[NaoBrancoValidadorErro,Any]:
                if len(valor.strip()) == 0:
                    return Either.erro(NaoBrancoValidadorErro(mensagem))
                return function(valor)
            return wrapper
        return decorator