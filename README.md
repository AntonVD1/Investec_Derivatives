# Investec Derivatives Pricing Models

This repository contains a collection of derivative pricing model stubs used by Investec.
The implementation focuses on creating a consistent interface for a variety of models.
The pricing logic still needs to be implemented for each model.

## Supported Models

| Model Name (Front Arena)                       | Scope     | Instruments / Notes                                                  |
| ---------------------------------------------- | --------- | ------------------------------------------------------------------- |
| Constant Debt to Equity instrument (CODEQ)     | In        | Confirm if there are live trades available                           |
| Credit basket linear                           | In        |                                                                     |
| Zero Coupon                                    | In        | Only need to test Cross currency swaps with long dated tenors        |
| Price Curve                                    | In        | Commodity                                                            |
| Commodity Asian Option                         | In        |                                                                     |
| Hazard Rate Model                              | In        | FX future/forward, Equity future/forward                             |
| Synthetic Underlying Forward                   | In        |                                                                     |
| Theoretical dividend futures                   | In        |                                                                     |
| Underlying Spot                                | In        |                                                                     |
| Black-Scholes                                  | Out       |                                                                     |
| Asian Arithmetic Fix MM                        | In        | Equity and FX Options                                                |
| Theoretical simple dividend option             | In        | Equity dividend option                                               |
| Total Return Swap                              | In        | Equity TRS                                                           |
| QEDI Variable Strike Warrant                   | In        |                                                                     |
| Convexity Adjusted Interest Rate Futures       | In        | FX barrier option, Equity barrier option                             |
| Barrier Continuous Analytic                    | In        |                                                                     |
| Discretised Barrier                            | In        |                                                                     |
| Index-Linked Bond Forward                      | In        |                                                                     |
| Fund Instrument                                | In        |                                                                     |
| Bond Futures                                   | Out       |                                                                     |
| Corporate Bond Model                           | In        |                                                                     |
| Theoretical dividend-neutral futures           | In        | Equity future/forward                                                |
| UDMC Cliquet Model                             | In        |                                                                     |
| Fully Funded TRS (Compound Model)              | In        |                                                                     |
| UseUnderlyingPrice                             | Out       |                                                                     |
| Finite Difference                              | In        | American Options on equity and FX underlyings incl. Barrier Options |
| Variable Strike Warrant Valuation              | Out       |                                                                     |
| Simple Tradeable Deposit                       | In        | ETF                                                                  |

Each model lives under `derivatives/models/` and exposes a `price()` method. The
models are grouped into subpackages (e.g. `options`, `bonds`, `futures`) to make
the repository easier to navigate. The current implementation simply raises
`NotImplementedError` as a placeholder for the actual pricing logic.
