
from unittest import TestCase
from maquina_bebidas import MaquinaBebidas

class TestBebidas(TestCase):

    def test_deve_retirar_bebida_e_diminuir_estoque(self):
        # Estoque inicial da maquina
        maquina = MaquinaBebidas()
        # Retirar 1 Coca-Cola
        estoque = maquina.retirar("Coca-Cola", {"Coca-Cola": 1})
        self.assertEqual({}, estoque)
