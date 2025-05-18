from .base import DerivativeModel

class ZeroCoupon(DerivativeModel):
    """Placeholder for the ZeroCoupon pricing logic."""

    def price(self, *args, **kwargs):
        """Compute price using ZeroCoupon model."""
        raise NotImplementedError("ZeroCoupon pricing not implemented")
