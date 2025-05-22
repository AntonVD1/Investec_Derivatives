from __future__ import annotations

import math

from ..base import DerivativeModel


class StaticHazardRateModel(DerivativeModel):
    """Static hazard rate model for expected default loss valuation.

    This implementation assumes a **constant** default intensity over the
    life of the exposure. More sophisticated alternatives include
    stepwise models (where the hazard rate changes at preset intervals) and
    stochastic models where the intensity follows a random process.
    """

    def price(
        self,
        notional: float,
        hazard_rate: float,
        maturity: float,
        discount_rate: float = 0.0,
    ) -> float:
        """Compute the discounted expected loss using a constant hazard rate.

        The underlying formula is::

            survival = exp(-hazard_rate * maturity)
            expected_loss = notional * (1 - survival)
            price = expected_loss * exp(-discount_rate * maturity)

        Parameters
        ----------
        notional:
            Exposure at default.
        hazard_rate:
            Constant hazard (default intensity) per annum.
        maturity:
            Time horizon in years.
        discount_rate:
            Risk-free discount rate used for present valuing the loss.

        Returns
        -------
        float
            Present value of the expected loss.
        """

        for name, value in {
            "notional": notional,
            "hazard_rate": hazard_rate,
            "maturity": maturity,
            "discount_rate": discount_rate,
        }.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"{name} must be numeric")
            if value < 0:
                raise ValueError(f"{name} cannot be negative")

        survival = math.exp(-hazard_rate * maturity)
        expected_loss = notional * (1.0 - survival)
        return expected_loss * math.exp(-discount_rate * maturity)
