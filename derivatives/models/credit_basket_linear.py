from __future__ import annotations

from typing import Iterable, Sequence

from .base import DerivativeModel


class CreditBasketLinear(DerivativeModel):
    """Linear credit basket model calculating expected default loss.

    The price is calculated as the sum of the expected losses of each name in
    the basket::

        price = sum(notional_i * p_i * (1 - recovery_i))

    where ``p_i`` is the probability of default derived from market spreads or
    a hazard rate model and ``recovery_i`` is the fractional recovery rate.
    """

    def price(
        self,
        notionals: Sequence[float],
        default_probabilities: Sequence[float],
        recovery_rates: Iterable[float] | None = None,
    ) -> float:
        """Compute price using a simple linear credit basket assumption.

        Parameters
        ----------
        notionals:
            Nominal amounts for each credit name in the basket.
        default_probabilities:
            Corresponding default probabilities for each credit name.
        recovery_rates:
            Fraction of notional recovered on default (defaults to zero for
            each name if not supplied).

        Returns
        -------
        float
            Present value of the expected credit losses.
        """

        notionals = list(notionals)
        probabilities = list(default_probabilities)
        if recovery_rates is None:
            recoveries = [0.0] * len(notionals)
        else:
            recoveries = list(recovery_rates)

        if not (len(notionals) == len(probabilities) == len(recoveries)):
            raise ValueError("Input sequences must have the same length")

        total = 0.0
        for n, p, r in zip(notionals, probabilities, recoveries):
            if not isinstance(n, (int, float)):
                raise TypeError("notional values must be numeric")
            if not isinstance(p, (int, float)):
                raise TypeError("default probabilities must be numeric")
            if not isinstance(r, (int, float)):
                raise TypeError("recovery rates must be numeric")
            if n < 0:
                raise ValueError("notional cannot be negative")
            if not 0.0 <= p <= 1.0:
                raise ValueError("default probability must be between 0 and 1")
            if not 0.0 <= r <= 1.0:
                raise ValueError("recovery rate must be between 0 and 1")

            total += n * p * (1.0 - r)

        return total
