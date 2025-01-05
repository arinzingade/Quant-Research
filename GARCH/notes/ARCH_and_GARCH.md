# [What are ARCH & GARCH Models](https://www.youtube.com/watch?v=P-_3M1LnIa8):

## Variance

1. Conditional Variance: measure of uncertainty about a variable given a set of information - variance that changes
2. *Heteroskedasticity: refers to the situation where the variance of errors is not constant across observations*

### Why Model Volatility?

![[Pasted image 20250105175809.png]]

Vol is much more predictable and also has a definitive pattern to it, making it easier to model.

## ARCH

1. AutoRegressive
2. It is a time series approach to modelling volatility that changes over time (conditional heteroskedasticity)
3. It tries to account for time dependency and "clustering" of volatility.
4. ![[Pasted image 20250103212620.png]]
5. ![[Pasted image 20250103212620.png]]
6. Estimating real world data typically means that we will have to large value of **q** 


## GARCH


1. GARCH is an attempt to generalize ARCH model

![[Pasted image 20250103213544.png]]

2. **GARCH(1,1):** Generalizes the EWMA, also assigning exponentially declining weights but in addition to that allowing us to model a long run variance towards which the series has tendency to pull and gravitate towards.
3. GARCH is inherently **mean reverting**
4. It does Forecasting
5. **Maximum likelihood estimation** in GARCH can be used to select the parameters.
6. ***Generalized** — It’s an expanded version of earlier models that were more limited in scope.*
7. ***Autoregressive** — It uses past values to predict future values.*
8. ***Conditional** — Its assumes that future volatility depends on information from the past.*
9. ***Heteroskedasticity** — It allows volatility to change over time (volatility is not constant). This means that it can handle periods of high (where prices are volatile) and low (where prices are stable) volatility.*


**[Assumptions and Properties](https://www.stavrianoseconblog.eu/2024/09/garch-models.html)**

The efficacy of the GARCH model hinges on several key assumptions and properties:

- **Stationarity**: For a GARCH model to provide meaningful and stable long-term forecasts, the series must be stationary. This typically requires that the sum of αiαi and βjβj be less than 1.
- **Volatility Clustering**: GARCH models assume that large changes in prices (either up or down) will be followed by large changes of either sign, which is a common attribute in financial time series.
- **Mean Reversion**: The models assume that volatility will revert to a long-term average over time, a behavior observed in many financial market volatilities.

An important feature of GARCH models is their ability to measure the persistence of volatility shocks. If the sum of the αα and ββ parameters is close to one, it suggests a high level of persistence, meaning that volatility shocks can affect volatility forecasts for a long time. This has profound implications for risk assessment and financial forecasting.

One of the primary challenges in using GARCH models is the risk of model misspecification. Selecting the wrong model form—whether it's the wrong type of GARCH model or inappropriate parameter values—can lead to inaccurate forecasts and misguided risk assessments. For instance, using a basic GARCH model when the data exhibits strong asymmetries or leverage effects might understate the actual risk involved, leading to potential financial losses.

**To mitigate these challenges, it is essential to conduct thorough data analysis and pre-processing to identify the most suitable GARCH model for the specific data set.**

[Successor to GARCH Models](https://www.reddit.com/r/quant/comments/m3102s/why_are_garch_models_used_in_academia_research/):
It’s been replaced mostly by stochastic volatility models. For valuing exotic derivatives, people often use the Heston model. Other IR/mean reverting models like SABR and CIR are good at modeling volatility directly. There are also other techniques like SVI