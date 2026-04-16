
from unittest import TestCase
from maquina_bebidas import MaquinaBebidas

class TestBebidas(TestCase):

    def test_deve_retirar_bebida_e_diminuir_estoque(self):
        maquina_bebidas = MaquinaBebidas()