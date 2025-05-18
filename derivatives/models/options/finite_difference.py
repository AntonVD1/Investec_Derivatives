"""Simple finite-difference solver for the Black--Scholes PDE."""

from math import exp

import numpy as np

from ..base import DerivativeModel

class FiniteDifference(DerivativeModel):
    """Explicit finite-difference pricer for European options."""

    def price(
        self,
        spot: float,
        strike: float,
        rate: float,
        vol: float,
        maturity: float,
        is_call: bool = True,
        s_max: float | None = None,
        n_time: int = 200,
        n_space: int = 200,
    ) -> float:
        """Solve the Black--Scholes PDE on a finite grid.

        Parameters
        ----------
        spot:
            Spot price of the underlying.
        strike:
            Option strike level.
        rate:
            Risk free interest rate.
        vol:
            Volatility of the underlying asset.
        maturity:
            Time to maturity in years.
        is_call:
            ``True`` for a call, ``False`` for a put.
        s_max:
            Maximum spot value considered in the grid. Defaults to ``2 * strike``.
        n_time:
            Number of time steps in the grid.
        n_space:
            Number of price steps in the grid.

        Returns
        -------
        float
            Approximation of the option price.
        """

        s_max = 2 * strike if s_max is None else s_max

        dt = maturity / n_time
        ds = s_max / n_space

        grid = np.zeros(n_space + 1)
        s_values = np.linspace(0, s_max, n_space + 1)

        if is_call:
            grid = np.maximum(s_values - strike, 0)
        else:
            grid = np.maximum(strike - s_values, 0)

        for _ in range(n_time):
            new_grid = grid.copy()
            for i in range(1, n_space):
                s = i * ds
                delta = (grid[i + 1] - grid[i - 1]) / (2 * ds)
                gamma = (grid[i + 1] - 2 * grid[i] + grid[i - 1]) / (ds**2)
                theta = (
                    -0.5 * vol**2 * s**2 * gamma
                    - rate * s * delta
                    + rate * grid[i]
                )
                new_grid[i] = grid[i] - dt * theta

            new_grid[0] = 0 if is_call else strike * exp(-rate * (_ * dt))
            new_grid[-1] = s_max - strike * exp(-rate * (_ * dt)) if is_call else 0
            grid = new_grid

        i = int(spot / ds)
        weight = (spot - i * ds) / ds
        price = grid[i] * (1 - weight) + grid[i + 1] * weight
        return float(price)
