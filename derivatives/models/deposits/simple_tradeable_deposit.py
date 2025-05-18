"""Model for a tradeable fixed-rate deposit."""

from ..base import DerivativeModel


class SimpleTradeableDeposit(DerivativeModel):
    """Accrued value of a simple deposit.

    Parameters
    ----------
    principal : float
        Initial amount deposited.
    rate : float
        Annual simple interest rate as a decimal.
    maturity : float
        Time to maturity in years.

    Notes
    -----
    The value ``V`` of a deposit accruing simple interest is given by::

        V = P * (1 + r * T)

    where ``P`` is the principal, ``r`` is the interest rate and ``T`` is the
    time in years.
    """

    def price(self, principal: float, rate: float, maturity: float) -> float:
        """Return the maturity value of the deposit."""

        return principal * (1 + rate * maturity)
