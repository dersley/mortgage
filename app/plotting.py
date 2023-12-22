from decimal import Decimal
import plotly.graph_objects as go

from lib.utils import time
from lib.mortgage import Mortgage

def plot_mortgage_payments(mortgage: Mortgage, monthly_payment: Decimal):

    start_date = mortgage.start_date
    end_date = mortgage.get_end_date()
    month_range = time.generate_monthly_dates(start_date, end_date)
    balance, interest = mortgage.pay_off_mortgage(monthly_payment)

    trace_1 = go.Scatter(x=month_range, y=interest, fill='tonexty', name='Interest', stackgroup="one")
    trace_2 = go.Scatter(x=month_range, y=balance, fill='tozeroy', name='Balance', stackgroup="one")

    # Create the figure and add traces
    fig = go.Figure()
    fig.add_trace(trace_2)
    fig.add_trace(trace_1)

    # Update layout
    fig.update_layout(title='Mortgage Payments Over Time',
                      xaxis_title='Date',
                      yaxis_title='Amount',
                      hovermode='x')


    return fig