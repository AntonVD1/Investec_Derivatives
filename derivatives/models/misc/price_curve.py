"""Simple price curve model using linear interpolation."""

from bisect import bisect_left

from ..base import DerivativeModel


class PriceCurve(DerivativeModel):
    """Linearly interpolated price curve.

    Parameters
    ----------
    times : list[float]
        Ordered time points in years.
    prices : list[float]
        Price at each time point.

    Notes
    -----
    Prices for intermediate times are obtained via linear interpolation between
    the two surrounding known points.
    """

    def __init__(self, times: list[float], prices: list[float]):
        self.times = times
        self.prices = prices

    def price(self, time: float) -> float:
        """Return the interpolated price at ``time``."""

        if not self.times:
            raise ValueError("Price curve has no data")

        if time <= self.times[0]:
            return self.prices[0]
        if time >= self.times[-1]:
            return self.prices[-1]

        idx = bisect_left(self.times, time)
        t0, t1 = self.times[idx - 1], self.times[idx]
        p0, p1 = self.prices[idx - 1], self.prices[idx]
        weight = (time - t0) / (t1 - t0)
        return p0 + weight * (p1 - p0)
