"""Continuously monitored barrier option priced via Monte Carlo."""

from math import exp

import numpy as np

from .base import DerivativeModel

class BarrierContinuousAnalytic(DerivativeModel):
    """Approximate pricer for continuously monitored barrier options."""

    def price(
        self,
        spot: float,
        strike: float,
        barrier: float,
        rate: float,
        vol: float,
        maturity: float,
        is_call: bool = True,
        barrier_type: str = "down-and-out",
        n_steps: int = 200,
        n_paths: int = 10_000,
    ) -> float:
        """Return the value of the barrier option using simulation.

        Parameters
        ----------
        spot:
            Current spot price.
        strike:
            Option strike level.
        barrier:
            Barrier level.
        rate:
            Risk free rate.
        vol:
            Volatility of the underlying.
        maturity:
            Time to maturity in years.
        is_call:
            ``True`` for a call option, ``False`` for a put.
        barrier_type:
            Either ``"down-and-out"`` or ``"up-and-out"``.
        n_steps:
            Number of monitoring steps used to approximate the continuous
            barrier.
        n_paths:
            Number of Monte Carlo paths.

        Returns
        -------
        float
            Present value of the barrier option.
        """

        dt = maturity / n_steps
        drift = (rate - 0.5 * vol ** 2) * dt
        diffusion = vol * np.sqrt(dt)

        payoffs = np.zeros(n_paths)
        for p in range(n_paths):
            price_path = spot
            knocked_out = False
            for _ in range(n_steps):
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
