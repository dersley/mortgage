import streamlit as st
from decimal import Decimal
import datetime as dt

from lib.address import Address
from lib.house import House
from lib.mortgage import Mortgage
from lib.utils import helper as h

from app import plotting as plot

st.set_page_config(layout="wide")

if "address" not in st.session_state:
    st.session_state.address = None
if "house" not in st.session_state:
    st.session_state.house = None
if "mortgage" not in st.session_state:
    st.session_state.mortgage = None

st.title("Mortgage Calculator")

seg1, seg2 = st.columns([0.4, 0.6])

property_expander = seg1.expander("Property Details", expanded=False)
with property_expander:

    def update_address_callback():
        st.session_state.address = Address(
            unit_number=address_dict["unit_number"],
            street_number=address_dict["street_number"],
            street_name=address_dict["street_name"],
            suburb=address_dict["suburb"],
            state=address_dict["state"],
            postcode=address_dict["postcode"],
            country=address_dict["country"],
        )

    address_form = st.form(key="address_form")
    with address_form:
        address_dict = {}
        col1, col2, col3 = st.columns([0.5, 0.25, 0.25])
        address_dict["street_name"] = col1.text_input("Street Name")
        address_dict["unit_number"] = col2.number_input(
            "Unit Number", min_value=0, max_value=10000
        )
        address_dict["street_number"] = col3.number_input(
            "Street Number", min_value=0, max_value=10000
        )
        address_dict["country"] = col1.text_input("Country")
        address_dict["suburb"] = col2.text_input("Suburb")
        address_dict["state"] = col3.text_input("State")
        address_dict["postcode"] = col3.number_input("Postcode", min_value=0)

        update_address_button = col1.form_submit_button(
            "Update Address", on_click=update_address_callback
        )

    house_form = st.form(key="house_form")
    with house_form:

        def update_house_callback():
            st.session_state.house = House(
                address=st.session_state.address,
                purchase_price=h.to_decimal(house_dict["purchase_price"]),
                current_value=h.to_decimal(house_dict["current_value"]),
            )

        house_dict = {}
        house_dict["purchase_price"] = st.number_input(
            "Purchase Price $AUD", min_value=0.0
        )
        house_dict["current_value"] = st.number_input(
            "Current Value $AUD", min_value=0.0
        )

        update_house_button = st.form_submit_button(
            "Update Valuation", on_click=update_house_callback
        )


mortgage_expander = seg1.expander("Mortgage Details", expanded=True)
with mortgage_expander:

    def update_mortgage_callback():
        st.session_state.mortgage = Mortgage(
            principle=h.to_decimal(mortgage_dict["principle"]),
            current_balance=h.to_decimal(mortgage_dict["current_balance"]),
            house=st.session_state.house,
            interest_rate=mortgage_dict["interest_rate"] / 100,
            start_date=mortgage_dict["start_date"],
            years=mortgage_dict["years"]
        )

    mortgage_form = st.form(key="mortgage_form")
    with mortgage_form:
        col1, col2 = st.columns(2)
        mortgage_dict = {}
        mortgage_dict["principle"] = col1.number_input("Principle $AUD", min_value=0.0)
        mortgage_dict["current_balance"] = col1.number_input("Current Balance $AUD", min_value=0.0)
        mortgage_dict["start_date"] = col2.date_input("Start Date")
        mortgage_dict["years"] = col2.selectbox("Mortgage Term (Years)", options=[5, 10, 20, 30])
        mortgage_dict["interest_rate"] = st.slider("Interest Rate", min_value=0.5, max_value=25.0, step=0.1)

        update_mortgage_button = st.form_submit_button(
            "Update Mortgage Details", on_click=update_mortgage_callback
        )

if st.session_state.mortgage is None:
    st.stop()

monthly_payment = seg2.slider("Monthly Payments $AUD", min_value=100.0, max_value=10000.0, step=100.0)
fig = plot.plot_mortgage_payments(st.session_state.mortgage, monthly_payment=h.to_decimal(monthly_payment))
seg2.plotly_chart(fig, use_container_width=True)