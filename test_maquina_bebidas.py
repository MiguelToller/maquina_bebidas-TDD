
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

    def test_deve_manter_consistencia_em_serie_de_operacoes(self):
        maquina = MaquinaBebidas(estoque_inicial={"Sprite": 5})

        maquina.abastecer("Sprite", 5) # 10 Sprites
        maquina.retirar("Sprite", 9)   # 1 Sprites
        maquina.abastecer("Agua", 3)   # 3 Aguas
        maquina.retirar("Agua", 1)     # 2 Aguas

        estoque_esperado = {"Sprite": 1, "Agua": 2}
        self.assertEqual(estoque_esperado, maquina.estoque)

    def test_deve_iniciar_com_estoque_vazio_quando_nenhum_parametro_e_passado(self):
        # Iniciando sem passar estoque_inicial (None)
        maquina = MaquinaBebidas()
        self.assertEqual({}, maquina.estoque)

    def test_deve_cadastrar_nova_bebida(self):
        maquina = MaquinaBebidas()
        maquina.cadastrar_bebida("Energetico")
        estoque = maquina.abastecer("Energetico", 5)
        self.assertEqual({"Energetico": 5}, estoque)

    def test_nao_deve_retirar_mais_que_o_estoque(self):
        maquina = MaquinaBebidas(estoque_inicial={"Coca-Cola": 1})
        with self.assertRaises(ValueError) as context:
            maquina.retirar("Coca-Cola", 2)
        self.assertEqual(MensagensErro.ESTOQUE_INSUFICIENTE, str(context.exception))

    def test_nao_deve_retirar_bebida_nao_cadastrada(self):
        maquina = MaquinaBebidas(estoque_inicial={"Sprite": 1})
        with self.assertRaises(ValueError) as context:
            maquina.retirar("Suco", 1)
        self.assertEqual(MensagensErro.BEBIDA_NAO_CADASTRADA, str(context.exception))

    def test_nao_deve_abastecer_bebida_nao_cadastrada(self):
        maquina = MaquinaBebidas(estoque_inicial={"Coca-Cola": 0})
        with self.assertRaises(ValueError) as context:
            maquina.abastecer("Suco", 5)
        self.assertEqual(MensagensErro.BEBIDA_NAO_CADASTRADA, str(context.exception))

    def test_nao_deve_iniciar_maquina_com_bebida_nao_cadastrada(self):
        with self.assertRaises(ValueError) as context:
            MaquinaBebidas(estoque_inicial={"Suco": 2})
        self.assertEqual(MensagensErro.BEBIDA_NAO_CADASTRADA, str(context.exception))

    def test_nao_deve_retirar_bebida_com_valor_negativo(self):
        maquina = MaquinaBebidas(estoque_inicial={"Sprite": 5})
        with self.assertRaises(ValueError) as context:
            maquina.retirar("Sprite", -1)
        self.assertEqual(MensagensErro.QUANTIDADE_INVALIDA, str(context.exception))

    def test_nao_deve_abastecer_bebida_com_valor_negativo(self):
        maquina = MaquinaBebidas(estoque_inicial={"Coca-Cola": 5})
        with self.assertRaises(ValueError) as context:
            maquina.abastecer("Coca-Cola", -1)
        self.assertEqual(MensagensErro.QUANTIDADE_INVALIDA, str(context.exception))

    def test_nao_deve_iniciar_maquina_com_estoque_negativo(self):
        with self.assertRaises(ValueError) as context:
            MaquinaBebidas(estoque_inicial={"Coca-Cola": -1})
        self.assertEqual(MensagensErro.QUANTIDADE_INVALIDA, str(context.exception))

    def test_nao_deve_aceitar_quantidade_zero(self):
        maquina = MaquinaBebidas(estoque_inicial={"Sprite": 5})
        
        with self.assertRaises(ValueError) as context_retirar:
            maquina.retirar("Sprite", 0)
        self.assertEqual(MensagensErro.QUANTIDADE_ZERO, str(context_retirar.exception))

        with self.assertRaises(ValueError) as context_abastecer:
            maquina.abastecer("Sprite", 0)
        self.assertEqual(MensagensErro.QUANTIDADE_ZERO, str(context_abastecer.exception))

    def test_nao_deve_cadastrar_bebida_com_nome_vazio(self):
        maquina = MaquinaBebidas()

        with self.assertRaises(ValueError) as context_1:
            maquina.cadastrar_bebida("") # String vazia
        self.assertEqual(MensagensErro.NOME_INVALIDO, str(context_1.exception))

        with self.assertRaises(ValueError) as context_2:
            maquina.cadastrar_bebida("  ") # String com espacos em branco
        self.assertEqual(MensagensErro.NOME_INVALIDO, str(context_2.exception))
