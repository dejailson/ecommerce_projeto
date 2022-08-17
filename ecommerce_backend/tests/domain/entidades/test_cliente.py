from app.domain.entidades import Cliente

class TestCliente():

    def test_deve_retornar_cliente_quando_fazer_cadastro(self):
        nome = 'Dejailson'
        sobrenome = 'Pinheiro'
        cpf = '475757575'
        cliente = Cliente(nome,sobrenome,cpf)
        assert cliente.nome == nome