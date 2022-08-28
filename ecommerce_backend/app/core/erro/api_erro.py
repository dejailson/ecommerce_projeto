class ApiErro(Exception):

    def __init__(self, mensagem: str, tipo_erro: str):
        Exception.__init__(self)
        self.__mensagem = mensagem
        self.__tipo_erro = tipo_erro

    @property
    def mensagem(self) -> str:
        return self.__mensagem

    @property
    def tipo_erro(self) -> str:
        return self.__tipo_erro
