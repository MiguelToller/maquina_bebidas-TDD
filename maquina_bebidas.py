
class MaquinaBebidas:

    def __init__(self, estoque_inicial: dict[str, int] = {}):
        self._estoque = estoque_inicial if estoque_inicial else {}
    
    def retirar(self, bebida, quantidade):
        self._estoque[bebida] -= quantidade
        return self._estoque