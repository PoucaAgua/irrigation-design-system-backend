from _decimal import Decimal


class ReferenceEvapotranspirationConstants:
    parameters_hargraves_samani = (Decimal(0.408), Decimal(0.0023), Decimal(17.8))
    parameters_blaney_cridlle  = (Decimal(0.457), Decimal(8.13), Decimal(100))
    parameters_penman_monteith  = (Decimal(0.408), Decimal(900), Decimal(273), Decimal(1), Decimal(0.34))