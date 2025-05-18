"""Zero-coupon bond pricing model."""

from math import exp

from .base import DerivativeModel


class ZeroCoupon(DerivativeModel):
    """Model for pricing a zero-coupon bond.

    Parameters
    ----------
    face_value : float
        Amount paid at maturity.
    discount_rate : float
        Continuously compounded annual interest rate.
    maturity : float
        Time to maturity in years.

    Notes
    -----
    The price ``P`` of a zero-coupon bond is given by::

        P = F * exp(-r * T)

    where ``F`` is the face value, ``r`` is the discount rate and ``T`` is the
    time to maturity.  See Hull, *Options, Futures, and Other Derivatives*.
    """

    def price(self, face_value: float, discount_rate: float, maturity: float) -> float:
        """Return the present value of the bond."""

        return face_value * exp(-discount_rate * maturity)
