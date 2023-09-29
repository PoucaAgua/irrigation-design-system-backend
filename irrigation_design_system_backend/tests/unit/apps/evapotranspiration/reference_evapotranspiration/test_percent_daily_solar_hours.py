from _decimal import Decimal
import pytest
from core.domain.enum.hemisphere import Hemisphere
from core.domain.enum.month import MonthEnum
from apps.evapotranspiration.reference_evapotranspiration.percent_daily_solar_hours import calculate_percent_daily_solar_hours  # Importe sua função

class TestCalculatePercentDailySolarHours:
    error = Decimal("1e-2")

    @pytest.mark.parametrize(
        "latitude, month, hemisphere, expected_result",
        [
            (53.0, MonthEnum.Jan, Hemisphere.NORTE, Decimal("17.8")),
            (53.0, MonthEnum.Jan, Hemisphere.SUL, Decimal("36.8")),
            (47.0, MonthEnum.Jan, Hemisphere.NORTE, Decimal("19.6")),
            (47.0, MonthEnum.Jan, Hemisphere.SUL, Decimal("34.4")),

            (32.0, MonthEnum.Fev, Hemisphere.NORTE, Decimal("25.0")),
            (32.0, MonthEnum.Fev, Hemisphere.SUL, Decimal("30.0")),
            (27.0, MonthEnum.Fev, Hemisphere.NORTE, Decimal("25.6")),
            (27.0, MonthEnum.Fev, Hemisphere.SUL, Decimal("29.4")),
            
            (13.0, MonthEnum.Mar, Hemisphere.NORTE, Decimal("25.0")),
            (13.0, MonthEnum.Mar, Hemisphere.SUL, Decimal("27.0")),
            (44.0, MonthEnum.Mar, Hemisphere.NORTE, Decimal("27.0")),
            (44.0, MonthEnum.Mar, Hemisphere.SUL, Decimal("28.0")),

            (6.0, MonthEnum.Abr, Hemisphere.NORTE, Decimal("28.0")),
            (6.0, MonthEnum.Abr, Hemisphere.SUL, Decimal("37.0")),
            (59.0, MonthEnum.Abr, Hemisphere.NORTE, Decimal("32.0")),
            (59.0, MonthEnum.Abr, Hemisphere.SUL, Decimal("22.2")),


            (42, MonthEnum.Mai, Hemisphere.NORTE, Decimal("32.8")),
            (18, MonthEnum.Mai, Hemisphere.SUL, Decimal("25.4")),
            (7, MonthEnum.Mai, Hemisphere.NORTE, Decimal("28")),
            (56, MonthEnum.Mai, Hemisphere.SUL, Decimal("17.82")),

        
            (23, MonthEnum.Jun, Hemisphere.NORTE, Decimal("30.6")),
            (48, MonthEnum.Jun, Hemisphere.SUL, Decimal("18.8")),
            (15, MonthEnum.Jun, Hemisphere.NORTE, Decimal("29.0")),
            (39, MonthEnum.Jun, Hemisphere.SUL, Decimal("21.2")),

            
            (10, MonthEnum.Jul, Hemisphere.NORTE, Decimal("29.0")),
            (35, MonthEnum.Jul, Hemisphere.SUL, Decimal("23.0")),
            (28, MonthEnum.Jul, Hemisphere.NORTE, Decimal("31")),
            (51, MonthEnum.Jul, Hemisphere.SUL, Decimal("18.6")),

            
            (5, MonthEnum.Ago, Hemisphere.NORTE, Decimal("28")),
            (61, MonthEnum.Ago, Hemisphere.SUL, Decimal("19.8")),
            (36, MonthEnum.Ago, Hemisphere.NORTE, Decimal("30.2")),
            (17, MonthEnum.Ago, Hemisphere.SUL, Decimal("26.0")),

            
            (13, MonthEnum.Set, Hemisphere.NORTE, Decimal("28.0")),
            (54, MonthEnum.Set, Hemisphere.SUL, Decimal("26.2")),
            (41, MonthEnum.Set, Hemisphere.NORTE, Decimal("28")),
            (3, MonthEnum.Set, Hemisphere.SUL, Decimal("27.0")),

            
            (33, MonthEnum.Out, Hemisphere.NORTE, Decimal("25.4")),
            (8, MonthEnum.Out, Hemisphere.SUL, Decimal("28.0")),
            (27, MonthEnum.Out, Hemisphere.NORTE, Decimal("26.0")),
            (49, MonthEnum.Out, Hemisphere.SUL, Decimal("30.8")),

            
            (19, MonthEnum.Nov, Hemisphere.NORTE, Decimal("25.2")),
            (45, MonthEnum.Nov, Hemisphere.SUL, Decimal("34.0")),
            (52, MonthEnum.Nov, Hemisphere.NORTE, Decimal("19.2")),
            (2, MonthEnum.Nov, Hemisphere.SUL, Decimal("27.4")),

            
            (26, MonthEnum.Dez, Hemisphere.NORTE, Decimal("23.8")),
            (58, MonthEnum.Dez, Hemisphere.SUL, Decimal("14.2")),
            (14, MonthEnum.Dez, Hemisphere.NORTE, Decimal("21.6")),
            (37, MonthEnum.Dez, Hemisphere.SUL, Decimal("32.8")),

        ],
    )
    def test_calculate_percent_daily_solar_hours(
        self, latitude, month, hemisphere, expected_result
    ):
        # When
        result = calculate_percent_daily_solar_hours(latitude, month, hemisphere)
        # Then
        assert abs(result - expected_result) <= self.error
