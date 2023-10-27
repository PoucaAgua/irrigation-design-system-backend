from _decimal import Decimal
import pytest
from core.domain.enum.hemisphere import Hemisphere
from core.domain.enum.month import MonthEnum
from apps.evapotranspiration.reference_evapotranspiration.reference_evapotranspiration_service import (
    ReferenceEvapotranspirationService,
)
from core.domain.entity.reference_evapotranspiration_input import (
    EToHargravesSamaniInput,
    EToBlanneyCriddleInput,
    EToPenmanMonteithInput,
)


class TestReferenceEvapotranspirationService:
    error = Decimal("1e-2")

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                EToHargravesSamaniInput(
                    temperature_med=Decimal("20.0"),
                    temperature_min=Decimal("10.0"),
                    temperature_max=Decimal("30.0"),
                    latitude=Decimal("69.0"),
                    month=MonthEnum.Jan,
                ),
                Decimal("22.165737965964677"),
            ),
            (
                EToHargravesSamaniInput(
                    temperature_med=Decimal("25.0"),
                    temperature_min=Decimal("30.0"),
                    temperature_max=Decimal("20.0"),
                    latitude=Decimal("44.0"),
                    month=MonthEnum.Dez,
                ),
                Decimal("18.05430705311771"),
            ),
            (
                EToHargravesSamaniInput(
                    temperature_med=Decimal("26.75"),
                    temperature_min=Decimal("30.4"),
                    temperature_max=Decimal("23.1"),
                    latitude=Decimal("13.0"),
                    month=MonthEnum.Mar,
                ),
                Decimal("13.267747880477849"),
            ),
        ],
    )
    def test_calculate_by_hargraves_samani(
        self, input_data: EToHargravesSamaniInput, expected_output
    ):
        result = ReferenceEvapotranspirationService.calculate_by_hargraves_samani(
            input_data
        )
        assert abs(result - expected_output) <= self.error

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                EToBlanneyCriddleInput(
                    temperature_med=Decimal("20.0"),
                    temperature_max=Decimal("30.0"),
                    temperature_min=Decimal("10.0"),
                    latitude=Decimal("31.0"),
                    month=MonthEnum.Jan,
                    hemisphere=Hemisphere.NORTE,
                ),
                Decimal("4.11026"),
            ),
        ],
    )
    def test_calculate_by_blaney_criddle(
        self, input_data: EToBlanneyCriddleInput, expected_output
    ):
        result = ReferenceEvapotranspirationService.calculate_by_blaney_criddle(
            input_data
        )
        assert abs(result - expected_output) <= self.error

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            (
                EToPenmanMonteithInput(
                    temperature_med=20.0,
                    temperature_max=30.0,
                    temperature_min=10.0,
                    days=30.0,
                    relative_humidity_air=50.0,
                    altitude=1.0,
                    wind_speed=20.0,
                    ground_heat=55.0,
                    daily_radiation=15.0,
                ),
                Decimal("10.026240268784955"),
            ),
        ],
    )
    def test_calculate_by_penman_monteith(
        self, input_data: EToPenmanMonteithInput, expected_output
    ):
        result = ReferenceEvapotranspirationService.calculate_by_penman_monteith(
            input_data
        )
        assert abs(result - expected_output) <= self.error
