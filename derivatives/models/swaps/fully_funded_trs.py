"""Pricing model for a fully funded total return swap."""

from math import exp

from ..base import DerivativeModel


class FullyFundedTRS(DerivativeModel):
    """Value a fully funded total return swap (compound model).

    Assumptions
    ----------
    * Funding and discounting use the same constant rate.
    * Dividends accrue continuously at a known yield.

    Payoff
    ------
    The holder receives ``S_T`` and pays back the funded amount
    ``S_0 * exp(funding_rate * T)``.
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
        """Return the present value of the fully funded TRS."""

        funded_amount = spot_price * exp(funding_rate * time_to_maturity)
        expected_asset = expected_terminal_price * exp(-dividend_yield * time_to_maturity)
        payoff = expected_asset - funded_amount
        return notional * payoff * exp(-funding_rate * time_to_maturity)
