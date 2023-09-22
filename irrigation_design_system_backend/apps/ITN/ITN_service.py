from _decimal import Decimal
from core.tables.df_test_table import df_test_table

class IrrigationTotalNecessaryService:
    @classmethod
    def __calculate_lixivation_fraction(cls, ce_i: Decimal, ce_e: Decimal) -> Decimal:
        return Decimal(ce_i / (2 * ce_e))


    @classmethod
    def calculate_by_fl(cls, input_entity) -> Decimal:
        irn = input_entity.irn
        ea = input_entity.ea
        fl = input_entity.fl
        return Decimal(irn / ((1 - fl) * ea))

    @classmethod
    def calculate_by_ce(cls, input_entity) -> Decimal:
        df_table = df_test_table()

        irn = input_entity.irn
        ce_i = input_entity.ce_i
        ce_e = input_entity.ce_e
        ea = input_entity.ea
        return Decimal(irn / ((1 - cls.__calculate_lixivation_fraction(ce_i, ce_e)) * ea))
