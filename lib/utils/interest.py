import numpy as np
from decimal import Decimal

def convert_yearly_to_monthly_interest(annual_rate: float) -> Decimal:
    """
    Convert an annual interest rate to a monthly rate.
    Input and output are in decimal format.
    """

    monthly_rate = (1 + annual_rate) ** (1/12) -1
    return monthly_rate
