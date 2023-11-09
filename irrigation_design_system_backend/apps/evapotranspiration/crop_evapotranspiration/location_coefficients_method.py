from _decimal import Decimal

import math


def calculate_by_keller(P: Decimal):
    return Decimal(P + Decimal(0.15) * (1 - P))


def calculate_by_bernardo(P: Decimal):
    return Decimal(P / 100)


def calculate_by_fereres(P: Decimal):
    return Decimal(P / 100)


def calculate_by_keller_and_bliesner(P):
    return Decimal(0.10 * math.sqrt(P))
