
[How to Use ACF and PACF to Identify Time Series Analysis Models](https://www.youtube.com/watch?v=CAT0Y66nPhs)

## Autocorrelation
**Autocorrelation** (also called serial correlation) is a statistical measure that describes the relationship between a variable's current value and its past values in a time series. Essentially, it indicates whether past values of the variable influence its future values.

---

## Why do ACF/PACF tests for GARCH?

- **ACF**: Reveals overall correlation between a time series and its lagged values at various time intervals.
- **PACF**: Focuses on the direct correlation of a time series with its lagged values, removing the influence of intermediate lags.


GARCH models assume that volatility is conditionally heteroskedastic and exhibits autocorreletion
over time.
ACF and PACF help detect these dependancies in the data, especially in the squared residuals or returns (a key input into the GARCH model).

IF there is no autocorrelation in the data, then there maybe no need of doing the GARCH modelling.

ACF of squared returns often reveals clustering by showing significant autocorrelation at certain lags. Significant autocorrelation in squared returns validates the use of a GARCH model to capture these patterns.

**For an Auto-Regressive Model, we need the Autocorrelation function (ACF) to exhibit the diminishing behavior overtime.**

![[Pasted image 20250106001908.png]]


### For PACF

![[Pasted image 20250106002008.png]]

If this is the graph we get, then we should start with an Auto-Regressive model with lags 1,2,3,10,13 because they are statistically significant as they are out of the blue zone.

---

For a model, GARCH (p, q)
the p value is given by the lags in the PACF plot
the q value is given by the lags in the ACF plot
