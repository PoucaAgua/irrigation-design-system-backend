from _decimal import Decimal


class ReferenceEvapotranspirationConstants:
    parameters_hargraves_samani = (Decimal(0.408), Decimal(0.0023), Decimal(17.8))
    parameters_blaney_cridlle = (Decimal(0.457), Decimal(8.13), Decimal(100))


class CropEvapotranspirationConstants:
    parameters_keller = (Decimal(0.15), Decimal(1))
    parameters_bernardo = Decimal(100)
    parameters_fereres = Decimal(100)
    parameters_keller_and_bliesner = Decimal(0.10)
