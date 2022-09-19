---
title: Lesser Known Backtesting Libraries
date: 2022-06-05
modified: 2022-09-18
status: Published
tags: trading, backtesting, crypto, algorythmic-trading, algotrading, quant
summary: This article presents set of lesser-known but interesing libraries that can be used for backtesting trading strategies and trading algortithms in general.
slug: lesser-known-backtesting-libraries
category: Algorithmic Trading
citation_needed: false
Image: /images/head/backtesting.jpg
---

<!-- MarkdownTOC levels='2,3' autolink=True autoanchor=True -->

- [Bt](#bt)
- [Blueshift](#blueshift)
- [AutoTrader](#autotrader)
- [Certis](#certis)
- [DeepCrypto](#deepcrypto)
- [TradingGym](#tradinggym)
- [vartests](#vartests)
- [backtesting-for-cryptocurrency-trading](#backtesting-for-cryptocurrency-trading)
- [Trade Engine](#trade-engine)
- [Epymetheus](#epymetheus)
- [TradzQAI](#tradzqai)
- [Stock Analysis Engine](#stock-analysis-engine)
- [BTGym](#btgym)
- [BakTst_Org](#baktst_org)
- [Stock-Portfolio-Backtester](#stock-portfolio-backtester)
- [Credits](#credits)

<!-- /MarkdownTOC -->

This article describe lesser-known python libraries/scripts that can be used for backtesting. [Here](https://safjan.com/popular-backtesting-libraries/) is list of most popular backtesting libraries that are excluded from scope of this article.

<a id="bt"></a>
## Bt
[Bt](https://github.com/pmorissette/bt) framework allows you to easily create strategies that mix and match different [`Algos`](https://pmorissette.github.io/bt/bt.html#bt.core.Algo "bt.core.Algo"). It aims to foster the creation of easily testable, re-usable and flexible blocks of strategy logic to facilitate the rapid development of complex trading strategies.

> The goal: to save **quants** from re-inventing the wheel and let them focus on the important part of the job - strategy development.


To recognise potential of this tool look at the [quick example](https://pmorissette.github.io/bt/#a-quick-example) provided by authors
The one of the interesting things that this library offers is [**tree structure of strategies**](https://pmorissette.github.io/bt/tree.html) - support for creative combining strategies.
The other reading focuses of composing optimal portfolio: [Flexible Backtesting with BT. Introducing bt — the open-sourced… | by Richard L | Medium](https://medium.com/@richardhwlin/flexible-backtesting-with-bt-7295c0dde5dd)
<a id="blueshift"></a>
## Blueshift
[Blueshift](https://blueshift.quantinsti.com/docs/) is to some extend free but not open source. You can research your ideas, backtest them, and take your strategies live with a broker of your choice on Blueshift. Blueshift helps you turn your ideas in to trading strategies.
Research and backtesting on the platform are free. Live strategy deployment is also free for a limited period.

<a id="autotrader"></a>
## AutoTrader
[AutoTrader](https://kieran-mackle.github.io/AutoTrader/) - A Python-based development platform for automated trading systems - from backtesting to optimisation to live-trading.
AutoTrader AutoTrader is Python-based platform intended to help in the development, optimisation and deployment of automated trading systems.

<a id="certis"></a>
## Certis
[Certis](https://github.com/Yeachan-Heo/Certis) "A High-Quality Backtesting Engine". If you want to learn about architecture of backtesting software you can definitely peek into [Certis repository](https://github.com/Yeachan-Heo/Certis) or my fork [here](https://github.com/izikeros/Certis)


<a id="deepcrypto"></a>
## DeepCrypto
[DeepCrypto](https://github.com/Yeachan-Heo/DeepCrypto) Rapid Backtesting via Numba Simple & Vectorized trading strategy maker builtin live trading features.

<a id="tradinggym"></a>
## TradingGym
[TradingGym](https://github.com/Yvictor/TradingGym) is a toolkit for training and backtesting the reinforcement learning algorithms. This was inspired by OpenAI Gym and imitated the framework form. Not only trading env but also has backtesting and in the future will implement realtime trading env with Interactive Broker API and so on.
This training environment originally design for tick-data, but also support for OHLC data format. WIP.

<a id="vartests"></a>
## vartests
 [vartests](https://github.com/rafa-rod/vartests) is a Python library to perform some statistical tests to evaluate Value at Risk (VaR) Models.

<a id="backtesting-for-cryptocurrency-trading"></a>
## backtesting-for-cryptocurrency-trading
[backtesting-for-cryptocurrency-trading](https://github.com/CyberPunkMetalHead/backtesting-for-cryptocurrency-trading) - you can use this simple crypto backtesting script to ensure your trading strategy is successful. Minimal setup required and works well with static TP and SL strategies. Trailing Stop Loss could improve profitability if added.

You can use this to determine how profitable your Binance Volatility bot is.
<a id="trade-engine"></a>
## Trade Engine
[Trade Engine](https://github.com/xibalbas/trade-engine) - a library for demo trading or backtest and forward test simulation.

<a id="epymetheus"></a>
## Epymetheus
[Epymetheus](https://github.com/epymetheus/epymetheus) is a multi-asset backtesting framework. It features an intuitive user API that lets analysts try out their trade strategies right away.


<a id="tradzqai"></a>
## TradzQAI
[TradzQAI](https://github.com/kkuette/TradzQAI) - Trading environment for RL agents, backtesting and training.


<a id="stock-analysis-engine"></a>
## Stock Analysis Engine
[Stock Analysis Engine](https://github.com/AlgoTraders/stock-analysis-engine). Build and tune investment algorithms for use with artificial intelligence (deep neural networks) with a distributed stack for running backtests using live pricing data on publicly traded companies with automated datafeeds from: IEX Cloud, Tradier and FinViz (includes: pricing, options, news, dividends, daily, intraday, screeners, statistics, financials, earnings, and more).


<a id="btgym"></a>
## BTGym
[BTGym](https://github.com/Kismuz/btgym). Scalable event-driven RL-friendly backtesting library. Build on top of Backtrader with OpenAI Gym environment API.


<a id="baktst_org"></a>
## BakTst_Org
[BakTst_Org](https://github.com/xiaoyao153379/BakTst_Org) is a prototype of the backtesting system used for BTC quantitative trading.


<a id="stock-portfolio-backtester"></a>
## Stock-Portfolio-Backtester
[Stock-Portfolio-Backtester](https://github.com/faizancodes/Stock-Portfolio-Backtester)
Efficient way to backtest optimized portfolio allocations for proper hedging techniques.

## Closing Thoughts
- I would like to look closer at [Epymetheus](https://github.com/epymetheus/epymetheus)
- I will definitely experiment with vectorbt

<a id="credits"></a>
## Credits
Heading photo from [unsplash](https://unsplash.com/photos/InWI1lteYfU) authored by [regularguy.eth](https://unsplash.com/@moneyphotos)