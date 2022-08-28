from functools import wraps
from typing import Any
from ...erro import Either
from .erros.nao_nulo_validador_erro import NaoNuloValidadorErro

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