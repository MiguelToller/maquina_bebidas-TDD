
class MaquinaBebidas:

    _BEBIDAS_VALIDAS = ["Coca-Cola", "Sprite", "Guarana", "Agua"]

    def __init__(self, estoque_inicial: dict[str, int] = None):
        self._estoque = estoque_inicial if estoque_inicial else {}

        for bebida in self._estoque.keys():
            if bebida not in self._BEBIDAS_VALIDAS:
                raise Exception("Bebida nao cadastrada")

    @property
    def estoque(self):
        return self._estoque
    
    def retirar(self, bebida, quantidade):
        # Verifica se a quantidade pedida e maior que o estoque atual
        # Caso nao ache a bebida retorna 0
        if quantidade > self._estoque.get(bebida, 0):
            raise Exception("Estoque insuficiente")
        self._estoque[bebida] -= quantidade
        return self._estoque
    
    def abastecer(self, bebida, quantidade):
        # Verifica se a bebida existe na maquina
        if bebida not in self._BEBIDAS_VALIDAS:
            raise Exception("Bebida nao cadastrada")
        # Utilizo o get para pegar a constante (caso a maquina comece vazia)
        estoque_atual = self._estoque.get(bebida, 0)
        self._estoque[bebida] = estoque_atual + quantidade

        return self._estoque