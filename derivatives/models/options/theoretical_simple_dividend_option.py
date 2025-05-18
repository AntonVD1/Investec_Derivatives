"""Simple model for options on a single dividend payment."""

from math import exp, log, sqrt

from scipy.stats import norm

from ..base import DerivativeModel

class TheoreticalSimpleDividendOption(DerivativeModel):
    """Black--Scholes style option on an anticipated dividend payment."""

    def price(
        self,
        expected_dividend: float,
        strike: float,
        rate: float,
        vol: float,
        maturity: float,
        is_call: bool = True,
    ) -> float:
        """Return the present value of the dividend option.

        Parameters
        ----------
        expected_dividend:
            Expected amount of the dividend at maturity.
        strike:
            Option strike level.
        rate:
            Continuously compounded risk free rate.
        vol:
            Volatility of the dividend forecast.
        maturity:
            Time to maturity in years.
        is_call:
            ``True`` for a call, ``False`` for a put.

        Returns
        -------
        float
            Present value of the option.
        """

        if vol <= 0 or maturity <= 0:
            intrinsic = max(expected_dividend - strike, 0.0)
            if not is_call:
                intrinsic = max(strike - expected_dividend, 0.0)
            return float(exp(-rate * maturity) * intrinsic)

        sqrt_t = sqrt(maturity)
        d1 = (log(expected_dividend / strike) + 0.5 * vol ** 2 * maturity) / (
            vol * sqrt_t
        )
        d2 = d1 - vol * sqrt_t

        df = exp(-rate * maturity)
        if is_call:
            price = expected_dividend * norm.cdf(d1) - strike * norm.cdf(d2)
        else:
            price = strike * norm.cdf(-d2) - expected_dividend * norm.cdf(-d1)

        return float(df * price)
