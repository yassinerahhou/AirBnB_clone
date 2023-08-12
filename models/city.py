#!/usr/bin/python3
"""the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent y.

    Attributes:
        state_id (str): The state id.
        name (str): name of the city.
    """

    state_id = ""
    name = ""
