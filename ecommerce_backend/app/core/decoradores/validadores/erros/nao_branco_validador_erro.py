from ....erro import ApiErro

class NaoBrancoValidadorErro(ApiErro):
    def __init__(self, mensagem: str):
        tipo_erro = 'NaoBrancoValidadorErro'
        super().__init__(mensagem=mensagem, tipo_erro=tipo_erro)