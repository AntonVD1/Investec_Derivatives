from __future__ import annotations

from ..base import DerivativeModel


class ConstantDebtToEquity(DerivativeModel):
    """Simple model for an instrument referencing a constant debt to equity ratio.

    The price is computed as::

        price = equity_price * (1 + debt_to_equity_ratio)

    This represents a linear payoff that increases proportionally with the
    underlying equity price and the specified debt/equity ratio.
    """

    def price(self, equity_price: float, debt_to_equity_ratio: float) -> float:
        """Compute price using a constant debt-to-equity relationship.

        Parameters
        ----------
        equity_price:
            Current price of the underlying equity.
        debt_to_equity_ratio:
            Ratio of debt relative to equity.

        Returns
        -------
        float
            Value of the instrument based on the simple formula above.
        """

        if not isinstance(equity_price, (int, float)):
            raise TypeError("equity_price must be numeric")
        if not isinstance(debt_to_equity_ratio, (int, float)):
            raise TypeError("debt_to_equity_ratio must be numeric")
        if equity_price < 0:
            raise ValueError("equity_price cannot be negative")
        if debt_to_equity_ratio < 0:
            raise ValueError("debt_to_equity_ratio cannot be negative")

        return equity_price * (1.0 + debt_to_equity_ratio)
