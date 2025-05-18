"""Simple corporate bond pricing model."""

from math import exp

from ..base import DerivativeModel


class CorporateBondModel(DerivativeModel):
    """Price a fixed-coupon corporate bond using continuous discounting.

    Parameters
    ----------
    face_value : float
        Amount paid at maturity.
    coupon_rate : float
        Annual coupon rate expressed as a decimal.
    yield_rate : float
        Continuously compounded yield to maturity.
    maturity : float
        Time to maturity in years.
    frequency : int, optional
        Number of coupon payments per year, default is ``1``.

    Notes
    -----
    The price is the present value of all coupons and the face value::

        P = \sum_{i=1}^{N} C \* exp(-y t_i) + F \* exp(-y T)

    where ``C`` is the coupon payment, ``y`` the yield and ``t_i`` the cash flow
    time.  See any standard fixed income text.
    """

    def price(
        self,
        face_value: float,
        coupon_rate: float,
        yield_rate: float,
        maturity: float,
        frequency: int = 1,
    ) -> float:
        """Return the price of the bond."""

        periods = int(maturity * frequency)
        coupon = face_value * coupon_rate / frequency
        value = 0.0
        for i in range(1, periods + 1):
            t = i / frequency
            value += coupon * exp(-yield_rate * t)
        value += face_value * exp(-yield_rate * maturity)
        return value
