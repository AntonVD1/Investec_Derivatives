"""Pricing model for dividend-neutral futures."""

from math import exp

from .base import DerivativeModel


class TheoreticalDividendNeutralFutures(DerivativeModel):
    """Compute the forward price ignoring dividend effects.

    Assumptions
    ----------
    * Constant risk-free rate and dividend yield.
    * No-arbitrage market.

    Payoff
    ------
    At maturity the contract pays ``notional * (S_T - F)`` with
    ``F = S_0 * exp(r * T)``.
    """

    def price(
        self,
        spot_price: float,
        risk_free_rate: float,
        time_to_maturity: float,
        notional: float = 1.0,
    ) -> float:
        """Return the forward price ignoring dividends."""

        forward_price = spot_price * exp(risk_free_rate * time_to_maturity)
        return notional * forward_price
