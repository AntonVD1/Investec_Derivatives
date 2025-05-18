"""Arithmetic Asian option pricer for commodity underlyings."""

from math import exp

import numpy as np

from .base import DerivativeModel

class CommodityAsianOption(DerivativeModel):
    """Monte Carlo pricer for arithmetic-average Asian options on commodities."""

    def price(
        self,
        spot: float,
        strike: float,
        rate: float,
        vol: float,
        maturity: float,
        num_obs: int,
        convenience_yield: float = 0.0,
        is_call: bool = True,
        n_paths: int = 10_000,
    ) -> float:
        """Return the option value.

        Parameters
        ----------
        spot:
            Current spot price of the commodity.
        strike:
            Option strike level.
        rate:
            Continuously compounded risk free rate.
        vol:
            Annualised volatility of the underlying.
        maturity:
            Time to maturity in years.
        num_obs:
            Number of equally spaced observation dates.
        convenience_yield:
            Convenience yield of the commodity.
        is_call:
            ``True`` for a call option, ``False`` for a put.
        n_paths:
            Number of Monte Carlo paths.

        Returns
        -------
        float
            Present value of the Asian option.
        """

        dt = maturity / num_obs
        drift = (rate - convenience_yield - 0.5 * vol ** 2) * dt
        diffusion = vol * np.sqrt(dt)

        payoffs = np.zeros(n_paths)
        for p in range(n_paths):
            price_path = spot
            running_sum = 0.0
            for _ in range(num_obs):
                price_path *= np.exp(drift + diffusion * np.random.normal())
                running_sum += price_path
            avg_price = running_sum / num_obs
            if is_call:
                payoffs[p] = max(avg_price - strike, 0.0)
            else:
                payoffs[p] = max(strike - avg_price, 0.0)

        return float(exp(-rate * maturity) * payoffs.mean())
