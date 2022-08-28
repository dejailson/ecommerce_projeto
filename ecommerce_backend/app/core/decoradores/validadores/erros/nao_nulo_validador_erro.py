from ....erro import ApiErro


class NaoNuloValidadorErro(ApiErro):

    def __init__(self, mensagem: str):
        tipo_erro = 'NaoNuloValidadorErro'
        super().__init__(mensagem=mensagem, tipo_erro=tipo_erro)
