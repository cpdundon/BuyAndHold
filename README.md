# BuyAndHold
Demonstrate the power for Buy and Hold investing

This project will establish the power of buy and hold investing.  A user's portfolio is matched up against a simple no fee index based portfolio.  This index portfolio is easy to implement via a discount broker.

A user will post their basic portfolio numbers (closing valuation and cash flow in/out).  Monthly IRR's will be calculated for the user portfolio and the risk of the user portfolio will be calculated too.  Risk is the standard deviation of the IRR returns.  

SPY returns will be pulled from Yahoo Finance.  Monthly IRR's will be calculated for a portfolio of (SPY and cash).  Here is the trick - the ratio of SPY to cash will be set so that the risk of the SPY/cash portfolio matches the user portfolio.  NOTE: for the present time the return of cash is assumed to be zero.   This assumption will be relaxed later.

Concluding finally: reconcile the user portfolio's total IRR against the SPY/cash total IRR.  We are comparing apples to apples as they both have the same risk.  The SPY/cash portfolio is expected to outperform.

-- Chris Dundon | 25-March-2015
