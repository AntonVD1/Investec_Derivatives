from __future__ import annotations

from .base import DerivativeModel


class FundInstrument(DerivativeModel):
    """Simple fund instrument priced as NAV multiplied by units held."""

    def price(self, nav: float, units: float) -> float:
        """Return the value of the fund position.

        Parameters
        ----------
        nav:
            Net asset value per unit of the fund.
        units:
            Number of units held.

        Returns
        -------
        float
            Value of the position.
        """

        if not isinstance(nav, (int, float)):
            raise TypeError("nav must be numeric")
        if not isinstance(units, (int, float)):
            raise TypeError("units must be numeric")
        if nav < 0:
            raise ValueError("nav cannot be negative")
        if units < 0:
            raise ValueError("units cannot be negative")

        return nav * units
