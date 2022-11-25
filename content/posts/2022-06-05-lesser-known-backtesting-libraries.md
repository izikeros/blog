---
title: Lesser Known Backtesting Libraries
date: 2022-06-05
modified: 2022-10-20
status: Published
tags: trading, backtesting, crypto, algorithmic-trading, algotrading, quant
summary: This article presents a set of lesser-known but interesting libraries that can be used for backtesting trading strategies and trading algorithms in general.
slug: lesser-known-backtesting-libraries
category: Algorithmic Trading
citation_needed: false
Image: /images/head/backtesting.jpg
---

<!-- MarkdownTOC levels='2,3' autolink=True autoanchor=True -->

- [Bt](#bt)
- [AutoTrader](#autotrader)
- [Blueshift](#blueshift)
- [Certis](#certis)
- [Epymetheus](#epymetheus)
- [DeepCrypto](#deepcrypto)
- [TradingGym](#tradinggym)
- [vartests](#vartests)
- [backtesting-for-cryptocurrency-trading](#backtesting-for-cryptocurrency-trading)
- [Trade Engine](#trade-engine)
- [TradzQAI](#tradzqai)
- [Stock Analysis Engine](#stock-analysis-engine)
- [BTGym](#btgym)
- [BakTst_Org](#baktst_org)
- [Stock-Portfolio-Backtester](#stock-portfolio-backtester)
- [QSTrader](#qstrader)
- [gemini](#gemini)
- [Closing Thoughts](#closing-thoughts)
- [Credits](#credits)

<!-- /MarkdownTOC -->

This article describes lesser-known python libraries/scripts that can be used for backtesting. [Here](https://safjan.com/popular-backtesting-libraries/) is a list of the most popular backtesting libraries that are excluded from the scope of this article. Actively developed libraries are in the top of the list.

<a id="bt"></a>
## Bt
![github stars shield](https://img.shields.io/github/stars/pmorissette/bt.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/pmorissette/bt)

[Bt](https://github.com/pmorissette/bt) framework allows you to easily create strategies that mix and match different [`Algos`](https://pmorissette.github.io/bt/bt.html#bt.core.Algo "bt.core.Algo"). It aims to foster the creation of easily testable, re-usable and flexible blocks of strategy logic to facilitate the rapid development of complex trading strategies.

> The goal: to save **quants** from re-inventing the wheel and let them focus on the important part of the job - strategy development.


To recognise potential of this tool look at the [quick example](https://pmorissette.github.io/bt/#a-quick-example) provided by authors
The one of the interesting things that this library offers is [**tree structure of strategies**](https://pmorissette.github.io/bt/tree.html) - support for creative combining strategies.
The other reading focuses of composing optimal portfolio: [Flexible Backtesting with BT. Introducing bt — the open-sourced… | by Richard L | Medium](https://medium.com/@richardhwlin/flexible-backtesting-with-bt-7295c0dde5dd)
**NOTE**: at the time of writing, Bt is in alpha stage
<a id="autotrader"></a>
## AutoTrader
![github stars shield](https://img.shields.io/github/stars/kieran-mackle/AutoTrader.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/kieran-mackle/AutoTrader)

[AutoTrader](https://kieran-mackle.github.io/AutoTrader/) - A Python-based development platform for automated trading systems - from backtesting to optimization to live-trading. AutoTrader is a Python-based platform intended to help in the development, optimization, and deployment of automated trading systems.

<a id="blueshift"></a>
## Blueshift
[Blueshift](https://blueshift.quantinsti.com/docs/) is to some extend free but not open source. You can research your ideas, backtest them, and take your strategies live with a broker of your choice on Blueshift. Blueshift helps you turn your ideas in to trading strategies.
Research and backtesting on the platform are free. Live strategy deployment is also free for a limited period.

<a id="certis"></a>
## Certis
![github stars shield](https://img.shields.io/github/stars/Yeachan-Heo/Certis.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/Yeachan-Heo/Certis)

[Certis](https://github.com/Yeachan-Heo/Certis) A Backtesting Engine. If you want to learn about the architecture of backtesting software you can definitely peek into [Certis repository](https://github.com/Yeachan-Heo/Certis)

<a id="epymetheus"></a>
## Epymetheus
![github stars shield](https://img.shields.io/github/stars/epymetheus/epymetheus.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/epymetheus/epymetheus)

[Epymetheus](https://github.com/epymetheus/epymetheus) is a multi-asset backtesting framework. It features an intuitive user API that lets analysts try out their trade strategies right away.

<a id="deepcrypto"></a>
## DeepCrypto
![github stars shield](https://img.shields.io/github/stars/Yeachan-Heo/DeepCrypto.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/Yeachan-Heo/DeepCrypto)

[DeepCrypto](https://github.com/Yeachan-Heo/DeepCrypto) Rapid Backtesting via Numba Simple & Vectorized trading strategy maker built-in live trading features.

<a id="tradinggym"></a>
## TradingGym
![github stars shield](https://img.shields.io/github/stars/Yvictor/TradingGym.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/Yvictor/TradingGym)

[TradingGym](https://github.com/Yvictor/TradingGym) is a toolkit for training and backtesting reinforcement learning algorithms. This was inspired by OpenAI Gym and imitated the framework form. Not only trading env but also has backtesting and in the future will implement real-time trading env with Interactive Broker API and so on.
This training environment originally designs for tick-data, but also supports for OHLC data format. 

<a id="vartests"></a>
## vartests
![github stars shield](https://img.shields.io/github/stars/rafa-rod/vartests.svg?logo=github)

 [vartests](https://github.com/rafa-rod/vartests) is a Python library to perform some statistical tests to evaluate Value at Risk (VaR) Models.

<a id="backtesting-for-cryptocurrency-trading"></a>
## backtesting-for-cryptocurrency-trading
![github stars shield](https://img.shields.io/github/stars/CyberPunkMetalHead/backtesting-for-cryptocurrency-trading.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/CyberPunkMetalHead/backtesting-for-cryptocurrency-trading) 

[backtesting-for-cryptocurrency-trading](https://github.com/CyberPunkMetalHead/backtesting-for-cryptocurrency-trading) - you can use this simple crypto backtesting script to ensure your trading strategy is successful. Minimal setup required and works well with static TP and SL strategies. Trailing Stop Loss could improve profitability if added.

You can use this to determine how profitable your Binance Volatility bot is.
<a id="trade-engine"></a>
## Trade Engine
![github stars shield](https://img.shields.io/github/stars/xibalbas/trade-engine.svg?logo=github)

[Trade Engine](https://github.com/xibalbas/trade-engine) - a library for demo trading or backtest and forward test simulation.

<a id="tradzqai"></a>
## TradzQAI
![github stars shield](https://img.shields.io/github/stars/kkuette/TradzQAI.svg?logo=github)

[TradzQAI](https://github.com/kkuette/TradzQAI) - Trading environment for RL agents, backtesting and training.


<a id="stock-analysis-engine"></a>
## Stock Analysis Engine
![github stars shield](https://img.shields.io/github/stars/AlgoTraders/stock-analysis-engine.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/AlgoTraders/stock-analysis-engine)

[Stock Analysis Engine](https://github.com/AlgoTraders/stock-analysis-engine). Build and tune investment algorithms for use with artificial intelligence (deep neural networks) with a distributed stack for running backtests using live pricing data on publicly traded companies with automated data feeds from: IEX Cloud, Tradier and FinViz (includes: pricing, options, news, dividends, daily, intraday, screeners, statistics, financials, earnings, and more).


<a id="btgym"></a>
## BTGym
![github stars shield](https://img.shields.io/github/stars/Kismuz/btgym.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/Kismuz/btgym)

[BTGym](https://github.com/Kismuz/btgym). Scalable event-driven RL-friendly backtesting library. Build on top of Backtrader with OpenAI Gym environment API.


<a id="baktst_org"></a>
## BakTst_Org
![github stars shield](https://img.shields.io/github/stars/xiaoyao153379/BakTst_Org.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/xiaoyao153379/BakTst_Org)

[BakTst_Org](https://github.com/xiaoyao153379/BakTst_Org) is a prototype of the backtesting system used for BTC quantitative trading.

<a id="stock-portfolio-backtester"></a>
## Stock-Portfolio-Backtester
![github stars shield](https://img.shields.io/github/stars/faizancodes/Stock-Portfolio-Backtester.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/faizancodes/Stock-Portfolio-Backtester)

[Stock-Portfolio-Backtester](https://github.com/faizancodes/Stock-Portfolio-Backtester)
Efficient way to backtest optimized portfolio allocations for proper hedging techniques.

<a id="qstrader"></a>
## QSTrader
![github stars shield](https://img.shields.io/github/stars/mhallsmoore/qstrader.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/mhallsmoore/qstrader)
[QSTrader](https://github.com/mhallsmoore/qstrader) is a free Python-based open-source modular schedule-driven backtesting framework for long-short equities and ETF-based systematic trading strategies.

<a id="gemini"></a>
## gemini
![github stars shield](https://img.shields.io/github/stars/anfederico/gemini.svg?logo=github) ![commit-activity](https://img.shields.io/github/commit-activity/y/mhallsmoore/qstrader)
[gemini](https://github.com/anfederico/gemini) - Backtesting for sleepless cryptocurrency markets

<a id="closing-thoughts"></a>
## Closing Thoughts
I would like to look closer at [Epymetheus](https://github.com/epymetheus/epymetheus)

<a id="credits"></a>
## Credits
Heading photo from [unsplash](https://unsplash.com/photos/InWI1lteYfU) authored by [regularguy.eth](https://unsplash.com/@moneyphotos)

*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*