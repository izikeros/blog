---
Category: note
Date: 2022-06-27
Modified: 2023-07-12
Slug: trading-algorithms
Status: published
Summary: This note contains a collection of trading algorithms or links to algorithms
Tags:
  - finance/algotrading
  - finance/crypto
  - algorithm
  - trading
  - strategies
  - finance
Title: Trading Algorithms and Trading Strategies
citation_needed: true
---
This note contains a collection of trading algorithms or links to algorithms

<!-- MarkdownTOC levels='2,3' autolink=True autoanchor=True -->

- [Momentum](#momentum)
- [Mean-Reversion](#mean-reversion)
- [Dynamic Hedging](#dynamic-hedging)
- [Volume-Weighted Average Price \(VWAP\)](#volume-weighted-average-price-vwap)
- [Algorithm libraries](#algorithm-libraries)
- [Other links](#other-links)

<!-- /MarkdownTOC -->

<a id="momentum"></a>

## Momentum

**Prices are up and we think they’ll continue to go up = Buy** (or vice versa).
Statistically, most momentum strategies don’t win particularly often but when they do win their gains are fairly large. Win:lose rates of around 55% with gain:loss of around 70% are fairly common with profitable algo’s.

The simplest TSM we can implement would require us to purchase the stock if it was up yesterday, and sell if it was down (if we’re holding it, otherwise we just wait).

**References:**

- [How to Get Started With Algorithmic Finance - KDnuggets](https://www.kdnuggets.com/2020/01/get-started-algorithmic-finance.html))
- Article with Description and code: [Algorithmic trading in less than 100 lines of Python code – O’Reilly](https://www.oreilly.com/content/algorithmic-trading-in-less-than-100-lines-of-python-code/)
- Moskowitz, Tobias, Yao Hua Ooi, and Lasse Heje Pedersen (2012): “Time Series Momentum.” Journal of Financial Economics, Vol. 104, 228-250.
- See repo: [trading-with-momentum](https://github.com/izikeros/trading-with-momentum)

<a id="mean-reversion"></a>

## Mean-Reversion

This is based on the idea that high and low prices of an asset will revert back to its mean (average) value. Once its price is below the mean, it is seen as an opportunity to buy the asset in hopes of the price going above its average. The average value of an asset constantly changes, so it requires constant monitoring.

***Prices are up but we think they’re due a pull-back = Sell*** (or vice versa).
 Conversely, most mean reversion strategies win more often than they lose however the gain to loss ratio is smaller. Win:lose rates of around 70% with gain:loss of around 55% are also pretty common with profitable algo’s.

<a id="dynamic-hedging"></a>

## Dynamic Hedging

from: [How to Get Started With Algorithmic Finance - KDnuggets](https://www.kdnuggets.com/2020/01/get-started-algorithmic-finance.html)

One investment fund that makes some of its strategies public is Invictus Capital’s [CRYPTO10 Hedged fund](https://invictuscapital.com/en/crypto10hedged), through its [litepaper](https://cdn.invictuscapital.com/whitepapers/c10-litepaper.pdf). In a one-line summary, the fund offers a “dynamic asset allocation strategy that dampens volatility and provides protection against losses.”

The fund fundamentally rebalances 10 assets, which can be seen as 10 data sources, in a manner analogous to the FTSE Russell Capping Methodology, discussed in depth [here](https://research.ftserussell.com/products/downloads/Capping_Methodology_Guide.pdf), which looks like this:

![img](https://i.ibb.co/TtjTwRm/Screenshot-2019-12-22-at-4-03-45-PM.png)Parameters of their base strategy include a rebalancing period and the number of constituent assets. So, we have insights into the data sources used, the algorithmic strategy, and the parameters. The paper even goes into the basics of the fitness function used:

![img](https://i.ibb.co/jVbgPDL/Screenshot-2019-12-22-at-4-12-41-PM.png)

In the above, *a**i* represents weight, and *Xi* represents a performance criterion. Maximizing the function yields a portfolio close to the “efficient frontier” - basically, the goal is to make the most money at the least risk.
> Read more on [FTSE Russell Capping Methodology](https://research.ftserussell.com/products/downloads/Capping_Methodology_Guide.pdf)

<a id="volume-weighted-average-price-vwap"></a>

## Volume-Weighted Average Price (VWAP)

This strategy breaks up a large order and releases dynamically determined smaller chunks of the order to the market using stock specific historical volume profiles. The aim is to execute the order close to the VWAP, thereby benefiting on the average price.

Time-weighted Average Price (TWAP)

The time-weighted average price strategy breaks up a large order and releases dynamically determined smaller chunks of the order to the market using evenly divided time slots between a start and end time. The aim is to execute the order close to the average price between the start and end times, thereby minimizing market impact.

See also:  [STOP Using Moving Averages! Anchored VWAP is the FUTURE in Day Trading - YouTube](https://www.youtube.com/watch?v=m7cL-TMKZpE)

<a id="algorithm-libraries"></a>

## Algorithm libraries

- [quantconnect strategy-library](https://www.quantconnect.com/tutorials/strategy-library/strategy-library) - each strategy is in form of tutorial with code, references. High quality.

> **NOTE:**
> These notes are bits collected from the internet. Proper attribution is needed.

<a id="other-links"></a>

## Other links

| link | description |
| --- | --- |
| [Algo-Trading-Strats](https://github.com/faizancodes/Algo-Trading-Strats)     |  Application of various algorithmic strategies to produce [[max_alpha|max alpha]]   |
| [sofienkaabar/Trend-Following-Strategies](https://github.com/sofienkaabar/Trend-Following-Strategies) | code for the book [Trend Following Strategies in Python; Kaabar, Sofien](https://www.amazon.com/Trend-Following-Strategies-Python-Indicators/dp/B09KNGG1CC)|
| [sofienkaabar/Contrarian-Trading-Strategies](https://github.com/sofienkaabar/Contrarian-Trading-Strategies) | code for the book [Contrarian Trading Strategies in Python; Kaabar, Sofien](https://www.amazon.com/Contrarian-Trading-Strategies-Python-Sofien/dp/B09VG3SH2P/)|
|[sofienkaabar/The-Book-of-Trading-Strategies](https://github.com/sofienkaabar/The-Book-of-Trading-Strategies) | code for the book [The Book of Trading Strategies;  Kaabar, Sofien](https://www.amazon.com/Book-Trading-Strategies-Sofien-Kaabar/dp/B09919GQ22)|
|[Crypto-Gamma-Scalping-](https://github.com/guiregueira/Crypto-Gamma-Scalping-)|Jupyter Notebook for scraping implementation and analysis, comments in Portugese|
|[Braavosi-Design/breakout-strategy](https://github.com/Braavosi-Design/breakout-strategy)||
|[70+ Trading Strategies (Free) – A List of Quantified Systems – Quantified Strategies For Traders](https://www.quantifiedstrategies.com/trading-strategies/) | multiple strategies described, often with accompanying backtesting |

[[heikin_ashi_candles_trading_scalping_strategy|Heikin-Ashi-based strategies]]

[[trading_strategies_playlist]]
