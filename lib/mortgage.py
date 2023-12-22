import numpy as np
from decimal import Decimal
import datetime as dt

from lib.house import House
from lib.utils import time, interest


class Mortgage:
    def __init__(
        self,
        principle: Decimal,
        current_balance: Decimal,
        house: House,
        interest_rate: Decimal,
        start_date: dt.date = dt.date.today(),
        years: int = 30,
    ):
        self.principle = principle
        self.current_balance = current_balance
        self.house = house
        self.interest_rate = interest_rate
        self.start_date = start_date
        self.years = years

    def get_deposit(self):
        """Return the original deposit for the property"""
        return self.house.purchase_price - self.principle
    
    def get_end_date(self):
        return time.add_years(self.start_date, years=self.years)
    
    def get_amount_paid_off(self):
        return self.principle - self.current_balance

    def calculate_minimum_monthly_repayment(self):
        pass

    def pay_off_mortgage(self, monthly_payment: Decimal):
        
        num_months = time.months_between(self.start_date, self.get_end_date())
        monthly_rate = interest.convert_yearly_to_monthly_interest(annual_rate=self.interest_rate)

        balance = np.zeros(num_months)
        interest_payments = np.zeros(num_months) 

        starting_balance = float(self.current_balance)
        for i in range(num_months):

            interest_payments[i] = starting_balance * monthly_rate
            starting_balance += interest_payments[i]
            balance[i] = starting_balance - float(monthly_payment)

            if balance[i] < 0:
                balance[i] = 0 
                break

            starting_balance = balance[i]

        balance = np.around(balance, 2)
        interest_payments = np.around(interest_payments, 2)

        return balance, interest_payments

    

