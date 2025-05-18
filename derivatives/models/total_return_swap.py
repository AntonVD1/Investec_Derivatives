"""Pricing model for a simple total return swap."""

from math import exp

from .base import DerivativeModel


class TotalReturnSwap(DerivativeModel):
    """Value a total return swap using a forward estimate of the underlying.

    Assumptions
    ----------
    * Constant funding rate and dividend yield.
    * The expected terminal price is provided and discounted at the funding
      rate.

    Payoff
    ------
    At maturity ``T`` the receiver of total return receives
    ``notional * (S_T - F_0)`` where ``F_0`` is the initial forward price.
    """

    def price(
        self,
        spot_price: float,
        expected_terminal_price: float,
        funding_rate: float,
        dividend_yield: float,
        time_to_maturity: float,
        notional: float = 1.0,
    ) -> float:
        """Return the present value of the total return swap."""

        initial_forward = spot_price * exp((funding_rate - dividend_yield) * time_to_maturity)
        payoff = expected_terminal_price - initial_forward
        return notional * payoff * exp(-funding_rate * time_to_maturity)
