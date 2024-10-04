from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .compra import (
    CompraSerializer,
    CriarEditarCompraSerializer,
    ListarCompraSerializer, # novo
    ItensCompraSerializer,
    CriarEditarItensCompraSerializer,
    ListarItensCompraSerializer, # novo
)
from .editora import EditoraSerializer
from .livro import LivroDetailSerializer, LivroListSerializer, LivroSerializer
from .user import UserSerializer

