"""Model for a simple index linked bond forward."""

from math import exp

from .base import DerivativeModel


class IndexLinkedBondForward(DerivativeModel):
    """Price a forward on an inflation index linked bond.

    Parameters
    ----------
    notional : float
        Principal amount of the bond.
    real_rate : float
        Continuously compounded real discount rate.
    maturity : float
        Time to maturity in years.
    index_ratio : float
        Ratio of the current index level to the base index level.

    Notes
    -----
    A forward price ``F`` on an index linked bond is commonly approximated by
    ``F = N * index_ratio * exp(-r * T)``, where ``N`` is the notional, ``r`` is
    the real rate and ``T`` is the time to maturity.
    """

    def price(
        self,
        notional: float,
        real_rate: float,
        maturity: float,
        index_ratio: float,
    ) -> float:
        """Return the forward price."""

        return notional * index_ratio * exp(-real_rate * maturity)
