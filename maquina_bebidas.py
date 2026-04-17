
class MaquinaBebidas:

    _BEBIDAS_VALIDAS = ["Coca-Cola", "Sprite", "Guarana", "Agua"]

    def __init__(self, estoque_inicial: dict[str, int] = None):
        self._estoque = estoque_inicial if estoque_inicial else {}

        for bebida, quantidade in self._estoque.items():
            if bebida not in self._BEBIDAS_VALIDAS:
                raise Exception("Bebida nao cadastrada")
            if quantidade < 0:
                raise Exception("Quantidade deve ser positiva")

    @property
    def estoque(self):
        return self._estoque
    
    def retirar(self, bebida, quantidade):
        if quantidade <= 0:
            raise Exception("Quantidade deve ser positiva")
        if bebida not in self._BEBIDAS_VALIDAS:
            raise Exception("Bebida nao cadastrada")
        
        # Pega o estoque atual e compara com a quantidade pedida
        estoque_atual = self._estoque.get(bebida, 0)
        if quantidade > estoque_atual:
            raise Exception("Estoque insuficiente")
        
        # Retira a bebida do estoque
        self._estoque[bebida] = estoque_atual - quantidade
        return self._estoque
    
    def abastecer(self, bebida, quantidade):
        if quantidade <= 0:
            raise Exception("Quantidade deve ser positiva")
        if bebida not in self._BEBIDAS_VALIDAS:
            raise Exception("Bebida nao cadastrada")
        
        # Abastece a bebida no estoque
        estoque_atual = self._estoque.get(bebida, 0)
        self._estoque[bebida] = estoque_atual + quantidade

        return self._estoque