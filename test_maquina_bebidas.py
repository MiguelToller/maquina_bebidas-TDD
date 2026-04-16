
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

    def test_deve_abastecer_bebida_e_aumentar_estoque(self):
        maquina = MaquinaBebidas(estoque_inicial={"Coca-Cola": 0})
        estoque = maquina.abastecer("Coca-Cola", 1)
        self.assertEqual({"Coca-Cola": 1}, estoque)

    def test_nao_deve_retirar_mais_que_o_estoque(self):
        maquina = MaquinaBebidas(estoque_inicial={"Coca-Cola": 1})
        with self.assertRaises(Exception) as context:
            maquina.retirar("Coca-Cola", 2)
        self.assertTrue("Estoque insuficiente" in str(context.exception))

    def test_nao_deve_retirar_bebida_nao_cadastrada(self):
        maquina = MaquinaBebidas(estoque_inicial={"Sprite": 1})
        with self.assertRaises(Exception) as context:
            maquina.retirar("Suco", 1)
        self.assertTrue("Bebida nao cadastrada" in str(context.exception))

    def test_nao_deve_abastecer_bebida_nao_cadastrada(self):
        maquina = MaquinaBebidas(estoque_inicial={"Coca-Cola": 0})
        with self.assertRaises(Exception) as context:
            maquina.abastecer("Suco", 5)
        self.assertTrue("Bebida nao cadastrada" in str(context.exception))

    def test_nao_deve_iniciar_maquina_com_bebida_nao_cadastrada(self):
        with self.assertRaises(Exception) as context:
            MaquinaBebidas(estoque_inicial={"Suco": 2})
        self.assertTrue("Bebida nao cadastrada" in str(context.exception))