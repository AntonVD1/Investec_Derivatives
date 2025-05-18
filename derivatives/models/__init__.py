"""Collection of derivative pricing models."""

from .base import DerivativeModel

# flake8: noqa

# Misc utilities
from .misc.constant_debt_to_equity import ConstantDebtToEquity
from .misc.price_curve import PriceCurve
from .misc.underlying_spot import UnderlyingSpot

# Credit models
from .credit.credit_basket_linear import CreditBasketLinear
from .credit.hazard_rate_model import HazardRateModel

# Bond models
from .bonds.zero_coupon import ZeroCoupon
from .bonds.index_linked_bond_forward import IndexLinkedBondForward
from .bonds.corporate_bond_model import CorporateBondModel

# Futures and forwards
from .futures.synthetic_underlying_forward import SyntheticUnderlyingForward
from .futures.theoretical_dividend_futures import TheoreticalDividendFutures
from .futures.theoretical_dividend_neutral_futures import TheoreticalDividendNeutralFutures
from .futures.convexity_adjusted_interest_rate_futures import ConvexityAdjustedInterestRateFutures

# Option models
from .options.asian_arithmetic_fix_mm import AsianArithmeticFixMM
from .options.commodity_asian_option import CommodityAsianOption
from .options.barrier_continuous_analytic import BarrierContinuousAnalytic
from .options.discretised_barrier import DiscretisedBarrier
from .options.qedi_variable_strike_warrant import QEDIVariableStrikeWarrant
from .options.theoretical_simple_dividend_option import TheoreticalSimpleDividendOption
from .options.udmc_cliquet_model import UDMCCliquetModel
from .options.finite_difference import FiniteDifference

# Swap models
from .swaps.total_return_swap import TotalReturnSwap
from .swaps.fully_funded_trs import FullyFundedTRS

# Deposit models
from .deposits.simple_tradeable_deposit import SimpleTradeableDeposit

# Fund models
from .funds.fund_instrument import FundInstrument
