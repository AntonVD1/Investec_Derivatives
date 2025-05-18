from .base import DerivativeModel

class UnderlyingSpot(DerivativeModel):
    """Placeholder for the UnderlyingSpot pricing logic."""

    def price(self, *args, **kwargs):
        """Compute price using UnderlyingSpot model."""
        raise NotImplementedError("UnderlyingSpot pricing not implemented")
