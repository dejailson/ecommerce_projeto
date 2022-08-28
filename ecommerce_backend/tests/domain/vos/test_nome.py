import pytest
from faker import Faker

from app.domain.vos import Nome
from app.core.decoradores.validadores.erros import NaoNuloValidadorErro


class TestNome():
    
    @pytest.fixture
    def nome(self):
        faker = Faker()
        return faker.name()

    def test_deve_retornar_joao_quando_criar_nome(self, nome):
        nome_faker = nome
        nome_erro = Nome.criar(nome_faker)
        nome = nome_erro.get()
        assert nome_erro.foi_concluido()
        assert nome.valor == nome_faker

    def test_deve_retornar_erro_quando_criar_nome_nulo(self):
        nome_erro = Nome.criar(None)
        erro = nome_erro.get()
        assert nome_erro.tem_erro()
        assert isinstance(erro, NaoNuloValidadorErro)
