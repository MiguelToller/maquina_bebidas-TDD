
from unittest import TestCase
from maquina_bebidas import MaquinaBebidas
from mensagens_erro import MensagensErro

class TestBebidas(TestCase):

    def test_deve_retirar_bebida_e_diminuir_estoque(self):
        maquina = MaquinaBebidas(estoque_inicial={"Coca-Cola": 1})
        estoque = maquina.retirar("Coca-Cola", 1)
        self.assertEqual({"Coca-Cola": 0}, estoque)

    def test_deve_abastecer_bebida_e_aumentar_estoque(self):
        maquina = MaquinaBebidas(estoque_inicial={"Coca-Cola": 0})
        estoque = maquina.abastecer("Coca-Cola", 1)
        self.assertEqual({"Coca-Cola": 1}, estoque)

    def test_nao_deve_retirar_mais_que_o_estoque(self):
        maquina = MaquinaBebidas(estoque_inicial={"Coca-Cola": 1})
        with self.assertRaises(ValueError) as context:
            maquina.retirar("Coca-Cola", 2)
        self.assertEqual(MensagensErro.ESTOQUE_INSUFICIENTE.value, str(context.exception))

    def test_nao_deve_retirar_bebida_nao_cadastrada(self):
        maquina = MaquinaBebidas(estoque_inicial={"Sprite": 1})
        with self.assertRaises(ValueError) as context:
            maquina.retirar("Suco", 1)
        self.assertEqual(MensagensErro.BEBIDA_NAO_CADASTRADA.value, str(context.exception))

    def test_nao_deve_abastecer_bebida_nao_cadastrada(self):
        maquina = MaquinaBebidas(estoque_inicial={"Coca-Cola": 0})
        with self.assertRaises(ValueError) as context:
            maquina.abastecer("Suco", 5)
        self.assertEqual(MensagensErro.BEBIDA_NAO_CADASTRADA.value, str(context.exception))

    def test_nao_deve_iniciar_maquina_com_bebida_nao_cadastrada(self):
        with self.assertRaises(ValueError) as context:
            MaquinaBebidas(estoque_inicial={"Suco": 2})
        self.assertEqual(MensagensErro.BEBIDA_NAO_CADASTRADA.value, str(context.exception))

    def test_nao_deve_retirar_bebida_com_valor_negativo(self):
        maquina = MaquinaBebidas(estoque_inicial={"Sprite": 5})
        with self.assertRaises(ValueError) as context:
            maquina.retirar("Sprite", -1)
        self.assertEqual(MensagensErro.QUANTIDADE_INVALIDA.value, str(context.exception))

    def test_nao_deve_abastecer_bebida_com_valor_negativo(self):
        maquina = MaquinaBebidas(estoque_inicial={"Coca-Cola": 5})
        with self.assertRaises(ValueError) as context:
            maquina.abastecer("Coca-Cola", -1)
        self.assertEqual(MensagensErro.QUANTIDADE_INVALIDA.value, str(context.exception))

    def test_nao_deve_iniciar_maquina_com_estoque_negativo(self):
        with self.assertRaises(ValueError) as context:
            MaquinaBebidas(estoque_inicial={"Coca-Cola": -1})
        self.assertEqual(MensagensErro.QUANTIDADE_INVALIDA.value, str(context.exception))