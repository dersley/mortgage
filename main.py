from decimal import Decimal
import datetime as dt
import matplotlib.pyplot as plt

from lib.address import Address
from lib.house import House
from lib.mortgage import Mortgage

from app import plotting


def main():

    address = Address(
        unit_number=1307,
        street_number=4,
        street_name="Edmondstone Street",
        suburb="South Brisbane",
        state="QLD",
        postcode=4101,
        country="Australia"
    )

    house = House(
        address=address,
        purchase_price=Decimal("400_000"),
        current_value=Decimal("500_000"),
    )

    mortgage = Mortgage(
        principle=Decimal("320_000"),
        current_balance=Decimal("287_332"),
        house=house,
        interest_rate=0.06,
        start_date=dt.date(2023, 1, 1),
        years=30
    )

    print(f"""

Address: {mortgage.house.address}
Purchase Price: $AUD {mortgage.house.purchase_price :.2f}
Current Estimated Value: $AUD {mortgage.house.current_value :.2f}
Deposit: $AUD {mortgage.get_deposit() :.2f}

Mortgage Principle: $AUD {mortgage.principle :.2f}
Remaining Balance: $AUD {mortgage.current_balance :.2f}
Amount Paid Off: $AUD {mortgage.get_amount_paid_off() :.2f}
Mortgage Term End: {mortgage.get_end_date()}

    """) 

    fig = plotting.plot_mortgage_payments(mortgage, monthly_payment=Decimal(2000))
    fig.show()

if __name__ == "__main__":
    main()