from _decimal import Decimal


def calculate_temperature_media(
    temperature_media: Decimal, temperature_max: Decimal, temperature_min: Decimal, days: Decimal
):
    if temperature_media is not None:
        return temperature_media

    if (
        temperature_max is not None
        and temperature_min is not None
        and days is not None
        and days != 0
    ):
        calculated_temperature_media = (temperature_max / days + temperature_min / days) / 2
        return calculated_temperature_media
