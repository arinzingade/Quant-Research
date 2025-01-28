

from __future__ import print_function

import datetime
import pickle
import warnings

from hmmlearn.hmm import GaussianHMM
from matplotlib import cm, pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator
import numpy as np
import pandas as pd
import seaborn as sns
import yfinance as yf


df = yf.download('BTC-USD', start='2014-01-01', end='2021-01-01')
df.columns = df.columns.droplevel(1)

def plot_in_sample_hidden_states(hmm_model, df):
    """
    Plot the adjusted closing prices masked by 
    the in-sample hidden states as a mechanism
    to understand the market regimes.
    """
    # Predict the hidden states array
    hidden_states = hmm_model.predict(rets)
    # Create the correctly formatted plot
    fig, axs = plt.subplots(
        hmm_model.n_components, 
        sharex=True, sharey=True
    )
    colours = cm.rainbow(
        np.linspace(0, 1, hmm_model.n_components)
    )
    for i, (ax, colour) in enumerate(zip(axs, colours)):
        mask = hidden_states == i
        ax.plot_date(
            df.index[mask], 
            df["Adj Close"][mask], 
            ".", linestyle='none', 
            c=colour
        )
        ax.set_title("Hidden State #%s" % i)
        ax.xaxis.set_major_locator(YearLocator())
        ax.xaxis.set_minor_locator(MonthLocator())
        ax.grid(True)
    plt.show()


df["Returns"] = df["Adj Close"].pct_change()
df = df.dropna()
rets = np.column_stack([df["Returns"]])

hmm_model = GaussianHMM(n_components=3, covariance_type="full", n_iter=1000).fit(rets)
print("Model Score:", hmm_model.score(rets))

plot_in_sample_hidden_states(hmm_model, df)

print("Pickling HMM model...")
pickle.dump(hmm_model, open("hmm_model.pkl", "wb"))
print("...HMM model pickled.")