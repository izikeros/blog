---
title: Lesser Known Backtesting Libraries
date: 2022-06-05
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
- [Credits](#credits)

<!-- /MarkdownTOC -->




<a id="bt"></a>
## Bt
[Bt](https://github.com/pmorissette/bt) framework allows you to easily create strategies that mix and match different [`Algos`](https://pmorissette.github.io/bt/bt.html#bt.core.Algo "bt.core.Algo"). It aims to foster the creation of easily testable, re-usable and flexible blocks of strategy logic to facilitate the rapid development of complex trading strategies.

> The goal: to save **quants** from re-inventing the wheel and let them focus on the important part of the job - strategy development.

https://github.com/pmorissette/bt

To recognize potential of this tool look at the [quick example](https://pmorissette.github.io/bt/#a-quick-example) provided by authors
The one of the interesting things that this library offers is tree structure of strategies - support for creative combinig strategies.

<a id="blueshift"></a>
## Blueshift
[Blueshift](https://blueshift.quantinsti.com/docs/) is to some extend free but not open source
https://blueshift.quantinsti.com/docs/

<a id="autotrader"></a>
## AutoTrader
A Python-based development platform for automated trading systems - from backtesting to optimisation to livetrading.
AutoTrader AutoTrader is Python-based platform intended to help in the development, optimisation and deployment of automated trading systems.

<a id="certis"></a>
## Certis
[Certis](https://github.com/Yeachan-Heo/Certis) "A High-Quality Backtesting Engine". If you want to learn about architecture of backtesing software you can definitely peek into [Certis repository](https://github.com/Yeachan-Heo/Certis) or my fork with changes intended to better maintain the code [here](https://github.com/izikeros/Certis)


<a id="deepcrypto"></a>
## DeepCrypto
[DeepCrypto](https://github.com/Yeachan-Heo/DeepCrypto) Rapid Backtesting via Numba Simple & Vectorized trading strategy maker bulitin live trading features.

<a id="tradinggym"></a>
## TradingGym
TradingGym is a toolkit for training and backtesting the reinforcement learning algorithms. This was inspired by OpenAI Gym and imitated the framework form. Not only traning env but also has backtesting and in the future will implement realtime trading env with Interactivate Broker API and so on.
This training env originally design for tickdata, but also support for ohlc data format. WIP.
https://github.com/Yvictor/TradingGym


<a id="vartests"></a>
## vartests
 is a Python library to perform some statistical tests to evaluate Value at Risk (VaR) Models.
https://github.com/rafa-rod/vartests

<a id="backtesting-for-cryptocurrency-trading"></a>
## backtesting-for-cryptocurrency-trading
You can use this simple crypto backtesting script to ensure your trading strategy is successful. Minimal setup required and works well with static TP and SL strategies. Trailing Stop Loss could imporove profitability if added.

For a detailed guide on how to set this up go to the main guide You can use this to determine how profitable your Binance Volatility bot is
https://github.com/CyberPunkMetalHead/backtesting-for-cryptocurrency-trading

<a id="trade-engine"></a>
## Trade Engine
a library for demo trading | backtest and forward test simulation for python >= 3.8
https://github.com/xibalbas/trade-engine

<a id="epymetheus"></a>
## Epymetheus
is a multi-asset backtesting framework. It features an intuitive user API that lets analysts try out their trade strategies right away.
https://github.com/epymetheus/epymetheus

<a id="tradzqai"></a>
## TradzQAI
Trading environnement for RL agents, backtesting and training.
https://github.com/kkuette/TradzQAI

<a id="stock-analysis-engine"></a>
## Stock Analysis Engine
Build and tune investment algorithms for use with artificial intelligence (deep neural networks) with a distributed stack for running backtests using live pricing data on publicly traded companies with automated datafeeds from: IEX Cloud, Tradier and FinViz (includes: pricing, options, news, dividends, daily, intraday, screeners, statistics, financials, earnings, and more).
https://github.com/AlgoTraders/stock-analysis-engine

<a id="btgym"></a>
## BTGym
Scalable event-driven RL-friendly backtesting library. Build on top of Backtrader with OpenAI Gym environment API.
https://github.com/Kismuz/btgym

<a id="baktst_org"></a>
## BakTst_Org
Introduction: BakTst_Org is a prototype of the backtesting system used for BTC quantitative trading.
https://github.com/xiaoyao153379/BakTst_Org


faizancodes / Stock-Portfolio-Backtester

<a id="credits"></a>
## Credits
Heading photo from [unsplash](https://unsplash.com/photos/InWI1lteYfU) authored by [regularguy.eth](https://unsplash.com/@moneyphotos)