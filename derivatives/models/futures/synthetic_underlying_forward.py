"""Pricing model for a synthetic underlying forward."""

from math import exp

from ..base import DerivativeModel


class SyntheticUnderlyingForward(DerivativeModel):
    """Compute the fair forward price using the cost-of-carry approach.

    Assumptions
    ----------
    * Constant risk-free rate and continuous dividend yield.
    * No transaction costs.

    Payoff
    ------
    At maturity :math:`T` the forward contract delivers
    ``notional * (S_T - F)`` where ``F`` is the forward price computed below.
    """

    def price(
        self,
        spot_price: float,
        risk_free_rate: float,
        dividend_yield: float,
        time_to_maturity: float,
        notional: float = 1.0,
    ) -> float:
        """Return the synthetic forward price.

        Parameters
        ----------
        spot_price:
            Current underlying spot price ``S_0``.
        risk_free_rate:
            Continuously compounded risk-free rate ``r``.
        dividend_yield:
            Continuous dividend yield ``q`` of the underlying.
        time_to_maturity:
            Time to delivery ``T`` in years.
        notional:
            Number of units of the underlying.
        """

        forward_price = spot_price * exp((risk_free_rate - dividend_yield) * time_to_maturity)
        return notional * forward_price
