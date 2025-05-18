"""Model for variable strike warrants using Black--Scholes."""

from math import exp, log, sqrt

from scipy.stats import norm

from .base import DerivativeModel

class QEDIVariableStrikeWarrant(DerivativeModel):
    """European warrant with strike proportional to the underlying spot."""

    def price(
        self,
        spot: float,
        strike_ratio: float,
        rate: float,
        vol: float,
        maturity: float,
        is_call: bool = True,
    ) -> float:
        """Return the theoretical value of the variable strike warrant.

        Parameters
        ----------
        spot:
            Current underlying price.
        strike_ratio:
            Ratio applied to the spot price to determine the strike at expiry.
        rate:
            Risk free rate.
        vol:
            Volatility of the underlying asset.
        maturity:
            Time to maturity in years.
        is_call:
            ``True`` for a call warrant, ``False`` for a put.

        Returns
        -------
        float
            The Black--Scholes value of the warrant.
        """

        strike = strike_ratio * spot
        sqrt_t = sqrt(maturity)
        d1 = (log(spot / strike) + (rate + 0.5 * vol ** 2) * maturity) / (vol * sqrt_t)
        d2 = d1 - vol * sqrt_t

        df = exp(-rate * maturity)
        if is_call:
            price = spot * norm.cdf(d1) - strike * df * norm.cdf(d2)
        else:
            price = strike * df * norm.cdf(-d2) - spot * norm.cdf(-d1)

        return float(price)
