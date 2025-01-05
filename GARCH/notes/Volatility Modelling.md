# [Volatility Modelling](https://www.youtube.com/watch?v=cDlbEQz1PQk&t=108s)

1. A model with a smaller error variance is better.

## Testing for Stationarity and Non-Stationarity.

### Dickey Fuller Test

1. Essentially to evaluate the time-series if it is consistent with the random walk.
2. A simple random walk is non-stationarity.

#### Stationarity

1. Stationarity revolves around the idea of consistency.
2. ![[Pasted image 20250105175809.png]]
3. ![[Pasted image 20250104193151.png]]
4. Distribution depends only on the difference in time and not the location of the time.
5. ![[Pasted image 20250104193533.png]]
6. If we pay close attention to the image above, the trending and the seasonal data, both are not stationary because:
	1. the mean of the time differentiated slots is not the same
	2. neither the variance is same.
7. **So how do we solve for data which is not stationary?***
8. *We can do Differencing.*
9. ![[Pasted image 20250104193712.png]]
10. *So above, we have made the mean consistent, but what about variance?*
11. ![[Pasted image 20250104193842.png]]
12. Differencing will not help us in making the variance stationary, so THEREFORE - we can model the variance itself using ARCH and GARCH, which makes them super useful.

---
## Volatility

**Definition:** Annualized standard deviation of the change in the price or value of a financial security.
### Estimation and Prediction Approaches

1. Poisson Jump diffusion model
2. ARCH / GARCH Model
3. Stochastic Volatility Models
4. Implied Volatility from Options

![[Pasted image 20250104201150.png]]


> [!NOTE] German Klass Paper
> The **Garman-Klass** volatility estimator is a financial model used to estimate the **volatility of an asset** based on its **high, low, opening, and closing prices** over a given time period. It was introduced by **Mark B. Garman** and **Michael J. Klass** in 1980 as an efficient way to estimate volatility using intraday price data

### Heteroskedasticity
**Heteroskedasticity** refers to the phenomenon in a statistical or econometric model where the **variance of the errors (residuals)** is **not constant** across observations. It is a violation of the assumption of **homoskedasticity**, which states that the error terms have constant variance.

---
### Autocorrelation
**Autocorrelation**, also known as **serial correlation**, is the correlation of a time series with its own past values. In simpler terms, it measures how well the current value of the series is related to its previous values at different time lags.

In **GARCH** modeling, we are often interested in modeling **volatility clustering** (where high volatility periods are followed by high volatility periods and low volatility periods are followed by low volatility periods). ACF and PACF plots help reveal if such clustering exists and can guide how you structure the model.

---
### Flow of Tests Before GARCH Modeling

1. [ ] **ADF Test**: Stationarity test.
2. [ ] **Phillips-Perron/KPSS Test**: Additional unit root tests.
3. [ ] **ACF/PACF Plots**: Check autocorrelation in data.
4. [ ] **ARCH LM Test**: Detect volatility clustering (heteroskedasticity).
5. [ ] **Ljung-Box Test**: Residual autocorrelation from mean model.
6. [ ] **Jarque-Bera Test**: Normality of residuals for GARCH innovations.
7. [ ] **White/Breusch-Pagan Test**: Check for heteroskedasticity in residuals.
8. [ ] **Model Order Selection**: AIC/BIC for GARCH model order.
9. [ ] **GARCH Estimation and Convergence**: Fit the model and check convergence.
10. [ ] **Post-GARCH Residual Analysis**: Validate residuals after GARCH.
11. [ ] **Forecast Validation**: Test the model’s out-of-sample forecasting ability.