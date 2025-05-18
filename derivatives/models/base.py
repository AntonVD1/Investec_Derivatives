"""Shared functionality for all derivative pricing models."""

from datetime import date
from typing import Union


class DerivativeModel:
    """Base class for derivative pricing models.

    In addition to defining the interface for ``price`` this class exposes
    several helper methods that simplify the implementation of concrete
    models:

    ``year_fraction``
        Compute the year fraction between two ``date`` instances using
        common day count conventions (``ACT/365``, ``ACT/360`` and ``30/360``).

    ``discount_factor``
        Calculate a simple discount factor from a continuously compounded
        or simple interest rate and two dates.  The helper relies on the
        ``year_fraction`` method for the day count calculation.

    ``validate_positive``
        Utility to ensure that numeric parameters are non-negative.  Models
        can call this during ``price`` to validate inputs.
    """

    # ------------------------------------------------------------------
    # Generic helpers
    # ------------------------------------------------------------------
    def year_fraction(
        self,
        start: date,
        end: date,
        convention: str = "act/365",
    ) -> float:
        """Return the day count fraction between ``start`` and ``end``.

        Parameters
        ----------
        start, end
            ``datetime.date`` objects representing the calculation period.
        convention
            Day count convention.  Supported values are ``"act/365"`` (the
            default), ``"act/360"`` and ``"30/360"``.
        """

        if not isinstance(start, date) or not isinstance(end, date):
            raise TypeError("start and end must be datetime.date instances")
        if end < start:
            raise ValueError("end must not be before start")

        days = (end - start).days
        if convention.lower() == "act/365":
            return days / 365.0
        if convention.lower() == "act/360":
            return days / 360.0
        if convention.lower() == "30/360":
            # 30/360 US convention
            d1 = min(start.day, 30)
            d2 = min(end.day, 30)
            months = (end.year - start.year) * 12 + (end.month - start.month)
            return ((months * 30) + (d2 - d1)) / 360.0

        raise ValueError(f"Unsupported day count convention: {convention}")

    def discount_factor(
        self,
        rate: float,
        start: date,
        end: date,
        convention: str = "act/365",
    ) -> float:
        """Compute a discount factor between ``start`` and ``end``.

        ``rate`` should be the annualised rate expressed as a decimal.  The
        function applies simple interest using the chosen day count
        convention.
        """

        self.validate_positive("rate", rate)
        tau = self.year_fraction(start, end, convention)
        return 1.0 / (1.0 + rate * tau)

    def validate_positive(self, name: str, value: Union[int, float]) -> None:
        """Validate that ``value`` is a non-negative number."""

        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number")
        if value < 0:
            raise ValueError(f"{name} must be non-negative")

    # ------------------------------------------------------------------
    # Interface
    # ------------------------------------------------------------------
    def price(self, *args, **kwargs):
        """Placeholder method for pricing logic."""
        raise NotImplementedError("Pricing logic not implemented")
