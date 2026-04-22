from enum import StrEnum

class MensagensErro(StrEnum):
    BEBIDA_NAO_CADASTRADA = "Bebida nao cadastrada"
    QUANTIDADE_INVALIDA = "Quantidade deve ser positiva"
    QUANTIDADE_ZERO = "Quantidade deve ser maior que 0"
    ESTOQUE_INSUFICIENTE = "Estoque insuficiente"
    NOME_INVALIDO = "Nome da bebida nao pode ser vazio"