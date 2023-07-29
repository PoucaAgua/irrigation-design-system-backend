from pydantic import BaseModel

# Resposta para sucesso na criação de um Crop Coefficient
class CropCoefficientCreateResponse(BaseModel):
    id: int
    culture_name: str
    coefficient_type: str
    coefficient_value: float

# Resposta para sucesso na recuperação de todos os Crop Coefficients
class CropCoefficientListResponse(BaseModel):
    coefficients: list[CropCoefficientCreateResponse]

# Resposta para erro
class ErrorResponse(BaseModel):
    error: str
