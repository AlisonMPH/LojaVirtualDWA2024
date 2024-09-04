from pydantic import field_validator
from models.pedido_model import EstadoPedido
from models.pedido_model import EstadoPedido
from util.validators import is_greater_than

class AlterarPedidoDto:
    id: int
    estado: EstadoPedido

    @field_validator("id_produto")
    def validar_id(cls, v):
        msg = is_greater_than(v, "Id do Produto", 0)
        if msg:
            raise ValueError(msg)
        return v