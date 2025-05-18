"""Discretely monitored barrier option priced via Monte Carlo."""

from math import exp

import numpy as np

from .base import DerivativeModel

class DiscretisedBarrier(DerivativeModel):
    """Monte Carlo pricer for discretely monitored barrier options."""

    def price(
        self,
        spot: float,
        strike: float,
        barrier: float,
        rate: float,
        vol: float,
        maturity: float,
        monitoring_times: int,
        is_call: bool = True,
        barrier_type: str = "down-and-out",
        n_paths: int = 10_000,
    ) -> float:
        """Return the value of the discretely monitored barrier option.

        Parameters
        ----------
        spot:
            Current spot price.
        strike:
            Strike of the option.
        barrier:
            Barrier level.
        rate:
            Risk free rate.
        vol:
            Volatility of the underlying.
        maturity:
            Time to maturity in years.
        monitoring_times:
            Number of equally spaced barrier observation dates.
        is_call:
            ``True`` for a call, ``False`` for a put.
        barrier_type:
            Either ``"down-and-out"`` or ``"up-and-out"``.
        n_paths:
            Number of Monte Carlo paths.

        Returns
        -------
        float
            Present value of the option.
        """

        dt = maturity / monitoring_times
        drift = (rate - 0.5 * vol ** 2) * dt
        diffusion = vol * np.sqrt(dt)

        payoffs = np.zeros(n_paths)
        for p in range(n_paths):
            price_path = spot
            knocked_out = False
            for _ in range(monitoring_times):
                price_path *= np.exp(drift + diffusion * np.random.normal())
                if barrier_type == "down-and-out" and price_path <= barrier:
                    knocked_out = True
                    break
                if barrier_type == "up-and-out" and price_path >= barrier:
                    knocked_out = True
                    break

            if not knocked_out:
                if is_call:
                    payoffs[p] = max(price_path - strike, 0.0)
                else:
                    payoffs[p] = max(strike - price_path, 0.0)

        return float(exp(-rate * maturity) * payoffs.mean())
