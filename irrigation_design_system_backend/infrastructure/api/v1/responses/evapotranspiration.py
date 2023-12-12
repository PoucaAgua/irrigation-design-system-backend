from infrastructure.api.v1.responses.response_model import OutputFloat


class EvapotranspirationResponse(OutputFloat):
    message: str = "Evapotranspiration calculation successful."
    value: float
