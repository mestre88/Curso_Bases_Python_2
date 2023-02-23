
import Ordenacao
import contatempos
import pytest

class Test_ordenacao:
    @pytest.fixture
    def ordena(self):
        a = Ordenacao.Ordenador()
        return a
    
    @pytest.fixture
    def l_quase(self):
        c = contatempos.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c = contatempos.ContaTempos()
        return c.lista_aleatoria(100)
    
    def esta_ordenada(self, lista):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                return False
        return True

    def test_bolha_curta_aleat(self, ordena, l_aleat):
        ordena.bolha_curta(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_selecao_direta_curta_aleat(self, ordena, l_aleat):
        ordena.selecao_direta(l_aleat)
        assert self.esta_ordenada(l_aleat)
    
    def testa_bolha_curta_quase(self, ordena, l_quase):
        ordena.bolha_curta(l_quase)
        assert self.esta_ordenada(l_quase)

    def testa_selecao_direta_curta_aleat(self, ordena, l_quase):
        ordena.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)

