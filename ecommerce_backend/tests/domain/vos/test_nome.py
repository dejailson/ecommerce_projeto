from app.domain.vos import Nome
import pytest

class TestNome():
    
    def test_deve_retornar_joao_quando_criar_nome(self):
        nome = Nome.criar('joao')
        assert nome.valor == 'joao'
    
    def test_deve_retornar_erro_quando_criar_nome_nulo(self):
        with pytest.raises(ValueError):
            Nome.criar(None)