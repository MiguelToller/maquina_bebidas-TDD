
from mensagens_erro import MensagensErro

class MaquinaBebidas:

    _BEBIDAS_VALIDAS = ["Coca-Cola", "Sprite", "Guarana", "Agua"]

    def __init__(self, estoque_inicial: dict[str, int] | None = None):
        self._estoque: dict[str, int] = estoque_inicial if estoque_inicial else {}
        self._validar_estoque()

    def _validar_estoque(self):
        for bebida, quantidade in self._estoque.items():
            if bebida not in self._BEBIDAS_VALIDAS:
                raise ValueError(MensagensErro.BEBIDA_NAO_CADASTRADA.value)
            if quantidade < 0:
                raise ValueError(MensagensErro.QUANTIDADE_INVALIDA.value)

    @property
    def estoque(self):
        return self._estoque
    
    def retirar(self, bebida: str, quantidade: int):
        if quantidade <= 0:
            raise ValueError(MensagensErro.QUANTIDADE_INVALIDA.value)
        if bebida not in self._BEBIDAS_VALIDAS:
            raise ValueError(MensagensErro.BEBIDA_NAO_CADASTRADA.value)
        
        # Pega o estoque atual e compara com a quantidade pedida
        estoque_atual = self._estoque.get(bebida, 0)
        if quantidade > estoque_atual:
            raise ValueError(MensagensErro.ESTOQUE_INSUFICIENTE.value)
        
        # Retira a bebida do estoque
        self._estoque[bebida] = estoque_atual - quantidade
        return self._estoque
    
    def abastecer(self, bebida: str, quantidade: int):
        if quantidade <= 0:
            raise ValueError(MensagensErro.QUANTIDADE_INVALIDA.value)
        if bebida not in self._BEBIDAS_VALIDAS:
            raise ValueError(MensagensErro.BEBIDA_NAO_CADASTRADA.value)
        
        # Abastece a bebida no estoque
        estoque_atual = self._estoque.get(bebida, 0)
        self._estoque[bebida] = estoque_atual + quantidade

        return self._estoque