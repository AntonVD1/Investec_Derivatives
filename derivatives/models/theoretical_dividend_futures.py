"""Pricing model for theoretical dividend futures."""

from math import exp
from typing import Iterable, Tuple

from .base import DerivativeModel


class TheoreticalDividendFutures(DerivativeModel):
    """Price a future on the stream of dividends of an underlying asset.

    Assumptions
    ----------
    * Constant risk-free rate.
    * Dividends are paid discretely at known future times.

    Payoff
    ------
    The contract pays the sum of dividends over ``[0, T]`` at maturity ``T``.
    """

    def price(
        self,
        dividends: Iterable[Tuple[float, float]],
        risk_free_rate: float,
        time_to_maturity: float,
        notional: float = 1.0,
    ) -> float:
        """Return the present value of the dividend future.

        Parameters
        ----------
        dividends:
            Iterable of ``(t, amount)`` pairs representing dividend payments.
        risk_free_rate:
            Continuously compounded risk-free rate ``r``.
        time_to_maturity:
            Contract maturity ``T`` in years. Payments beyond ``T`` are ignored.
        notional:
            Scaling factor for the dividend stream.
        """

        pv = 0.0
        for t, amount in dividends:
            if t <= time_to_maturity:
                pv += amount * exp(-risk_free_rate * t)
        return notional * pv
