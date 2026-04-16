
class MaquinaBebidas:

    def __init__(self, estoque_inicial: dict[str, int] = None):
        self._estoque = estoque_inicial if estoque_inicial else {}

    @property
    def estoque(self):
        return self._estoque
    
    def retirar(self, bebida, quantidade):
        self._estoque[bebida] -= quantidade
        return self._estoque
    
    def abastecer(self, bebida, quantidade):
        self._estoque[bebida] += quantidade
        return self._estoque