from decimal import Decimal
from pydantic import BaseModel


class ETcInput(BaseModel):
    P: Decimal  # Adicione a anotação de tipo Decimal ao atributo P
    # Outros atributos da classe
