
class MaquinaBebidas:

    def __init__(self, estoque_inicial: dict[str, int] = None):
        self._estoque = estoque_inicial if estoque_inicial else {}

    @property
    def estoque(self):
        return self._estoque
    
    def retirar(self, bebida, quantidade):
        # Verifica se a quantidade pedida e maior que o estoque atual
        if quantidade > self._estoque.get(bebida, 0):
            raise Exception("Estoque insuficiente")
        self._estoque[bebida] -= quantidade
        return self._estoque
    
    def abastecer(self, bebida, quantidade):
        self._estoque[bebida] += quantidade
        return self._estoque