from .base import DerivativeModel

class FiniteDifference(DerivativeModel):
    """Placeholder for the FiniteDifference pricing logic."""

    def price(self, *args, **kwargs):
        """Compute price using FiniteDifference model."""
        raise NotImplementedError("FiniteDifference pricing not implemented")
