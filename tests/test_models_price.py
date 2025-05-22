import pytest

from derivatives import models

MODEL_CLASSES = [
    models.DerivativeModel,
    models.ConstantDebtToEquity,
    models.CreditBasketLinear,
    models.ZeroCoupon,
    models.PriceCurve,
    models.CommodityAsianOption,
    models.StaticHazardRateModel,
    models.SyntheticUnderlyingForward,
    models.TheoreticalDividendFutures,
    models.UnderlyingSpot,
    models.AsianArithmeticFixMM,
    models.TheoreticalSimpleDividendOption,
    models.TotalReturnSwap,
    models.QEDIVariableStrikeWarrant,
    models.ConvexityAdjustedInterestRateFutures,
    models.BarrierContinuousAnalytic,
    models.DiscretisedBarrier,
    models.IndexLinkedBondForward,
    models.FundInstrument,
    models.CorporateBondModel,
    models.TheoreticalDividendNeutralFutures,
    models.UDMCCliquetModel,
    models.FullyFundedTRS,
    models.FiniteDifference,
    models.SimpleTradeableDeposit,
]


@pytest.mark.parametrize("model_cls", MODEL_CLASSES)
def test_price_not_implemented_default(model_cls):
    """Ensure price() raises NotImplementedError without arguments."""
    model = model_cls()
    with pytest.raises(NotImplementedError):
        model.price()


@pytest.mark.parametrize("model_cls", MODEL_CLASSES)
def test_price_not_implemented_with_parameters(model_cls):
    """Ensure price() raises NotImplementedError with various arguments."""
    model = model_cls()
    # Typical numeric example
    with pytest.raises(NotImplementedError):
        model.price(spot=100, strike=100, maturity=1.0)
    # Edge case with invalid values
    with pytest.raises(NotImplementedError):
        model.price(spot=-100, maturity=-1.0, extra=None)
