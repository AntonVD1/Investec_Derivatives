from __future__ import annotations

from typing import Iterable

from ..base import DerivativeModel


class UDMCCliquetModel(DerivativeModel):
    """Simplified Cliquet option model using cap and floor on periodic returns."""

    def price(
        self,
        returns: Iterable[float],
        cap: float,
        floor: float,
        notional: float = 1.0,
    ) -> float:
        """Price a cliquet option with uniform cap and floor per period.

        Parameters
        ----------
        returns:
            Sequence of periodic returns of the underlying.
        cap:
            Maximum payoff per period.
        floor:
            Minimum payoff per period.
        notional:
            Notional amount of the option.

        Returns
        -------
        float
            Sum of capped and floored returns multiplied by the notional.
        """

        if cap < floor:
            raise ValueError("cap must be greater than or equal to floor")
        if not isinstance(notional, (int, float)):
            raise TypeError("notional must be numeric")
        if notional < 0:
            raise ValueError("notional cannot be negative")

        processed_returns = []
        for r in returns:
            if not isinstance(r, (int, float)):
                raise TypeError("returns must contain numeric values")
            processed_returns.append(r)

        payoff = 0.0
        for r in processed_returns:
            payoff += min(max(r, floor), cap)

        return notional * payoff
