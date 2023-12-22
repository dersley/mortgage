from dataclasses import dataclass

@dataclass
class Address:
    unit_number: int
    street_number: int
    street_name: str
    suburb: str
    state: str
    postcode: int
    country: int
