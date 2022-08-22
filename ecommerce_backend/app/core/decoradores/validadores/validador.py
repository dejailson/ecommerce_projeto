from functools import wraps
class Validador():
      
    @classmethod
    def nao_nulo_validador(cls,mensagem):
        def decorator(function):
            @wraps(function)
            def wrapper(valor):
                if valor is None:
                    raise ValueError(mensagem)
                return function(valor)
            return wrapper
        return decorator