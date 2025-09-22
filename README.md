# Equity Insights Engine: 5 Years, 10 Tickers, Monthly Stats & Volatility Deciles  

## Overview  
This project analyzes 5 years of daily stock market data for 10 major companies using Python and the yFinance library.  
It computes key monthly statistics, evaluates risk, and identifies periods of extreme volatility. The goal is to demonstrate data handling, financial analytics, and portfolio insights using Python and Pandas.  

---

## Features  
- Collects 5 years of daily price and volume data for 10 stocks.  
- Calculates:  
  - Average monthly closing price  
  - Average shares traded per month  
  - Average dollar volume traded per month  
  - Average monthly return  
  - Standard deviation of monthly returns  
- Identifies:  
  - Stock with the highest monthly return  
  - Stock with the highest return volatility  
- Reports top and bottom decile months by daily volatility with dollar volume.  
- Outputs all statistics in a consolidated Pandas DataFrame.  

---

## Technologies Used  
- Python 3.10+  
- pandas  
- yfinance  

---

## How It Works  
1. Fetches daily price and volume data using yfinance.  
2. Resamples into monthly statistics (close, volume, returns).  
3. Calculates average monthly metrics and risk measures.  
4. Detects extreme volatility months (top 10% and bottom 10%).  
5. Prints consolidated analysis results.  

---

## Example Outputs  
- Daily Data: Raw stock prices, returns, and dollar volumes.  
- Monthly Analysis DataFrame: Summary metrics for each ticker.  
- Insights:  
  - Stock with highest average monthly return.  
  - Stock with highest return standard deviation.  
- Volatility Deciles: High and low volatility months with corresponding dollar volumes.  
