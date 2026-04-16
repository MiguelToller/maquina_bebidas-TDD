
from unittest import TestCase
from maquina_bebidas import MaquinaBebidas

class TestBebidas(TestCase):

    def test_deve_retirar_bebida_e_diminuir_estoque(self):
        # Estoque inicial da maquina
        maquina = MaquinaBebidas(estoque_inicial={"Coca-Cola": 1})
        # Retirar a bebida (nome do produto, quantidade)
        estoque = maquina.retirar("Coca-Cola", 1)
        # Comparacao do retorno com o estoque
        self.assertEqual({"Coca-Cola": 0}, estoque)
