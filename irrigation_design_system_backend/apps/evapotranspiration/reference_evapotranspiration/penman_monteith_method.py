import math


def calculate_vapor_saturation_pressure(temperature):
    es = 0.6108 * math.exp((17.27 * temperature) / (temperature + 237.3))
    return es


def calculate_vapor_current_pressure(relative_humidity_air, vapor_saturation_pressure):
    ea = (relative_humidity_air / 100) * vapor_saturation_pressure
    return ea


def calculate_declivity_curve_pressure_vapor(temperature, vapor_saturation_pressure):
    delta = (4098 * vapor_saturation_pressure) / ((temperature + 237.3) ** 2)
    return delta


def calculate_atmospheric_pressure(altitude):
    atmospheric_pressure = 101.3 * (293 - 0.0065 * altitude / 293.0) ** 5.23
    return atmospheric_pressure


def calculate_psychrometric_constant(atmospheric_pressure):
    gamma = 0.665 * 10**-3 * atmospheric_pressure
    return gamma
