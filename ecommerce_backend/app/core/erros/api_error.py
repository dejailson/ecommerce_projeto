class ApiErro(Exception):

    def __init__(self, message:str, tipo_erro:str):
        Exception.__init__(self)
        self.message = message
        self.tipo_erro = tipo_erro