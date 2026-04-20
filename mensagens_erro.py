from enum import Enum
from dataclasses import dataclass

@dataclass(frozen=True)
class MensagensErro(Enum):
    BEBIDA_NAO_CADASTRADA: str = "Bebida nao cadastrada"
    QUANTIDADE_INVALIDA: str = "Quantidade deve ser positiva"
    QUANTIDADE_ZERO: str = "Quantidade deve ser maior que 0"
    ESTOQUE_INSUFICIENTE: str = "Estoque insuficiente"