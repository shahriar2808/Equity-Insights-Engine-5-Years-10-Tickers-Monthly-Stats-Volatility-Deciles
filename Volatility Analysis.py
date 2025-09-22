"""
Task List

1) Read 5 years of daily stock data for 10 companies from yfinance.

2) For each stock calculate:
   - Average monthly closing price
   - Average shares traded per month
   - Average dollar volume traded per month
   - Average monthly return
   - Standard deviation of monthly returns

3) Save all the above statistics in a single Pandas DataFrame and print it.

4) Report:
   - The stock with the highest average monthly return
   - The stock with the highest monthly return standard deviation

5) For each stock, identify the months in the top and bottom deciles according to daily volatility.
   - Report the dollar volume for these months
"""

# Importing libraries

import yfinance as yf
import pandas as pd


# Task: Read 5 years of daily data for 10 tickers

TICKERS = ("AAPL", "TSLA", "MCD", "GOOG", "AMZN",
           "HD", "AEO", "BA", "JPM", "WFC")

SAMPLE_LEN = "5y" #Defining the length of the time

# Creating empty lists which Will store raw daily 
# and monthly data for all tickers

daily_list = []
monthly_list = []
volatility_list = []

for tic in TICKERS:
    print(f"Processing raw data for {tic}")

# Building daily data for all tickers

    daily = yf.Ticker(tic).history(SAMPLE_LEN)
    daily["Ticker"] = tic
    daily["Daily_ret"] = daily["Close"].pct_change()
    daily["Dollar_Vol"] = daily["Close"] * daily["Volume"]
    daily_list.append(daily)

# Building monthly data for all tickers
    # Creating an Empty DataFrame to store monthly data
    monthly = pd.DataFrame()
    
    # month-end closing price
    monthly["Close"] = daily["Close"].resample("1ME").last()
    
    # monthly total shares traded 
    monthly["Vol"] = daily["Volume"].resample("1ME").sum()
    
    # monthly total $ volume
    monthly["Dollar_vol"] = daily["Dollar_Vol"].resample("1ME").sum()
    
    # monthly % return from month-end closes
    monthly["Return"] = monthly["Close"].pct_change()
    monthly["Ticker"] = tic
    monthly_list.append(monthly)

# Building volatility data

    # Calculating monthly volatility based on daily-return
    mvol = daily["Daily_ret"].resample("1ME").std() 
    # Creating an Empty DataFrame to store the volatility data
    df_mvol = pd.DataFrame()
    # Putting the month-end dates to identify the months
    df_mvol["Month"] = mvol.index
    df_mvol["Ticker"] = tic
    # Returning the monthly volatility values in the column named volatility in this dataframe
    df_mvol["Volatility"] = mvol.values
    # Returning the dollar volume values in the column named Dollar_vol in this dataframe
    df_mvol["Dollar_vol"] = monthly["Dollar_vol"].values
    

    bottom_decile = df_mvol["Volatility"].quantile(0.10)
    top_decile = df_mvol["Volatility"].quantile(0.90)
    bottom = df_mvol[df_mvol["Volatility"] <= bottom_decile].copy()
    bottom["Decile"] = "bottom 10%"

    top = df_mvol[df_mvol["Volatility"] >= top_decile].copy()
    top["Decile"] = "top 10%"

    volatility_list.append(pd.concat([bottom, top], ignore_index=True))



# Combining all tickers in daily and monthly DataFrames

daily_data = pd.concat(daily_list)
monthly_data = pd.concat(monthly_list)
volatility_data = pd.concat(volatility_list)

print()
print("==Daily Stock Data of 10 Companies==")
print()
print(daily_data)
print()

# Task: Calculating Monthly Data for each Stock

print("==Calculating Monthly Stock Data==")
print()

analysis = pd.DataFrame()

# Average monthly closing price
analysis["avg_month_close"] = monthly_data.groupby("Ticker")["Close"].mean()

# Average shares traded per month 
analysis["avg_trade"] = monthly_data.groupby("Ticker")["Vol"].mean()

# Average dollar volume traded per month
analysis["avg_dollar_vol"] = monthly_data.groupby("Ticker")["Dollar_vol"].mean()

# Average monthly return
analysis["avg_month_ret"] = monthly_data.groupby("Ticker")["Return"].mean()

# Standard deviation of monthly returns
analysis["month_std"] = monthly_data.groupby("Ticker")["Return"].std()

# Task: Saving the above in a Single Pandas DataFrame

print(analysis)
print()

# Task: Reporting Highest Monthly Return & Standard Deviation

print("==Stock with Highest Monthly Return & STDev==")
print()

# Identifying the Stock with the highest Monthly Return
top_stock = analysis["avg_month_ret"].idxmax() # Using .idxmax() to return the highest index

# Returning the Return Value for the highest Monthly Return
top_ret = analysis["avg_month_ret"].max()

# Identifying the Stock with the highest Monthly Standard Deviation
risk_stock = analysis["month_std"].idxmax() # Using .idxmax() to return the highest index

# Returning the STDev Value for the highest Monthly STDev
stock_std = analysis["month_std"].max()

print(f"Stock with the Highest Monthly Return is {top_stock} and Return is {top_ret:.2%}")
print()
print(f"Stock with the Highest Monthly Return STDev is {risk_stock} and STDev {stock_std:.2f}")
print()

# Task: Calculating Volatility and Return

print("==Top and Bottom Volatility Deciles==")
print(volatility_data)

# For requirement 5b, I am currently unsure about the best way 
# to structure the initial coding plan. 
# Therefore, I have not attempted this step at this stage.