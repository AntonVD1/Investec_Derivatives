"""Model representing the underlying spot price."""

from ..base import DerivativeModel


class UnderlyingSpot(DerivativeModel):
    """Return the spot price of the underlying asset.

    The model assumes the current spot price is observable and no additional
    adjustments are required.
    """

    def price(self, spot_price: float, notional: float = 1.0) -> float:
        """Return ``notional * spot_price``."""

        return notional * spot_price
