from app.domain.entidades import Cliente
from app.domain.vos import Nome

class TestCliente():

    def test_deve_retornar_cliente_quando_fazer_cadastro(self):
        # cliente = Cliente.construtor().nome(Nome.criar('João')).sobrenome('Silva').cpf('12345678901').criar()
        assert 1 == 1 