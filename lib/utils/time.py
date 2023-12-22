import datetime as dt
from dateutil.relativedelta import relativedelta


def add_years(start_date: dt.date, years: int):
    return start_date + relativedelta(years=years)


def months_between(start_date: dt.date, end_date: dt.date) -> int:
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    delta = relativedelta(end_date, start_date)
    return delta.years * 12 + delta.months + 1


def generate_monthly_dates(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += relativedelta(months=1)
    return dates