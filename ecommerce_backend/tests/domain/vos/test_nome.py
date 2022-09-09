import pytest
from faker import Faker

from app.domain.vos import Nome
from app.core.decoradores.validadores.erros import NaoNuloValidadorErro
from app.core.decoradores.validadores.erros import NaoBrancoValidadorErro


class TestNome():
    
    @pytest.fixture
    def nome(self):
        faker = Faker()
        return faker.name()

    def test_deve_retornar_sucesso_quando_criar_nome(self, nome):
        nome_faker = nome
        nome_erro = Nome.criar(nome_faker)
        nome = nome_erro.get()
        assert nome_erro.foi_concluido()
        assert nome.valor == nome_faker

    def test_deve_retornar_erro_quando_criar_nome_nulo(self):
        nome_erro = Nome.criar(None)
        erro = nome_erro.get()
        mensagem = 'não pode ser nulo'
        assert nome_erro.tem_erro()
        assert mensagem in erro.mensagem
        assert isinstance(erro, NaoNuloValidadorErro)
    
    def test_deve_retornar_nao_branco_validador_erro_quando_criar_nome_em_branco(self):
        nome_branco = "  "
        nome_erro = Nome.criar(nome_branco)
        erro = nome_erro.get()
        assert nome_erro.tem_erro()
        assert isinstance(erro,NaoBrancoValidadorErro)
