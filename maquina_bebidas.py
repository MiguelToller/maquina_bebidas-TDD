
from mensagens_erro import MensagensErro

class MaquinaBebidas:
    """
    Maquina de bebidas que gerencia o estoque de produtos.
    """

    def __init__(self, estoque_inicial: dict[str, int] | None = None):
        """
        Inicializa a maquina com um estoque opcional.

        Args:
            estoque_inicial: Dicionario onde a chave e o nome da bebida e o valor e a quantidade.
        """
        self._bebidas_validas = ["Coca-Cola", "Sprite", "Guarana", "Agua"]

        self._estoque: dict[str, int] = estoque_inicial.copy() if estoque_inicial else {}
        self._validar_estoque()

    def _validar_estoque(self) -> None:
        """
        Verifica se o estoque inicial possui bebidas e quantidade validas.

        Raises:
            ValueError: Se a bebida nao estiver cadastrada ou a quantidade for negativa.
        """
        for bebida, quantidade in self._estoque.items():
            if bebida not in self._bebidas_validas:
                raise ValueError(MensagensErro.BEBIDA_NAO_CADASTRADA)
            if quantidade < 0:
                raise ValueError(MensagensErro.QUANTIDADE_INVALIDA)

    def _validar_operacao(self, bebida: str, quantidade: int) -> None:
        """
        Valida se a quantidade e a bebida sao validas para qualquer operacao.

        Args:
            bebida: Nome da bebida.
            quantidade: Quantidade da bebida escolhida. 

        Raises:
            ValueError: Se a quantidade for igual a 0, menor que 0 ou a bebida for invalida.
        """
        if quantidade == 0:
            raise ValueError(MensagensErro.QUANTIDADE_ZERO)
        if quantidade < 0:
            raise ValueError(MensagensErro.QUANTIDADE_INVALIDA)
        if bebida not in self._bebidas_validas:
            raise ValueError(MensagensErro.BEBIDA_NAO_CADASTRADA)

    @property
    def estoque(self) -> dict[str, int]:
        """
        Retorna uma copia do estado atual do estoque.
        """
        return self._estoque.copy()
    
    def retirar(self, bebida: str, quantidade: int) -> dict[str, int]:
        """
        Retira uma determinada quantidade de uma bebida do estoque.

        Args:
            bebida: Nome da bebida a ser retirada.
            quantidade: Quantidade a ser retirada (deve ser > que 0).

        Returns:
            Copia do dicionario atualizado com o estoque.

        Raises:
            ValueError: Se tentar retirar mais que o estoque,
                        Se a quantidade ou a bebida forem invalidas.
        """
        self._validar_operacao(bebida, quantidade)
        
        estoque_atual = self._estoque.get(bebida, 0)
        if quantidade > estoque_atual:
            raise ValueError(MensagensErro.ESTOQUE_INSUFICIENTE)
        
        self._estoque[bebida] = estoque_atual - quantidade
        return self._estoque.copy()
    
    def abastecer(self, bebida: str, quantidade: int) -> dict[str, int]:
        """
        Abastece o estoque com uma determinada quantidade de bebida.

        Args:
            bebida: Nome da bebida a ser abastecida.
            quantidade: Quantidade a ser abastecida (deve ser > que 0).

        Returns:
            Copia do dicionario atualizado com o estoque.

        Raises:
            ValueError: Se a quantidade ou a bebida forem invalidas.
        """
        self._validar_operacao(bebida, quantidade)
        
        estoque_atual = self._estoque.get(bebida, 0)
        self._estoque[bebida] = estoque_atual + quantidade

        return self._estoque.copy()
    
    def cadastrar_bebida(self, bebida: str) -> None:
        """
        Cadastra uma nova bebida no sistema.

        Args:
            bebida: Nome da bebida a ser cadastrada.

        Raises:
            ValueError: Se o nome da bebida for vazio ou conter espacos.
        """
        if not bebida.strip():
            raise ValueError(MensagensErro.NOME_INVALIDO)
        
        bebida_normalizada = bebida.strip().title()

        if bebida_normalizada not in self._bebidas_validas:
            self._bebidas_validas.append(bebida_normalizada)