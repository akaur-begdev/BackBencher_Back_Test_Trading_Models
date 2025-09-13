import yfinance as yf
import pandas

print("-----")
ticker = input("Which ticker would you like to do the back-testing for?")
data = yf.download(ticker, start='2020-01-01', end='2025-01-01')
print(data.info())
print(data.head())

print("-----")
type_of_data = type(data)
print(f"The data type is {type_of_data}.")

print("-----")
closing_data = data[["Close"]]
print(closing_data)

print("-----")
data["MarketRet"] = data["Close"].pct_change()
print(data)

print("-----")
data["Action"] = data["MarketRet"]>0
print(data)

print("-----")
data["Action"] = data["Action"].astype(int)
print(data)

data["Action"] = data["Action"].shift(1).fillna(0)

print("-----")
data["StratRet"] = data["MarketRet"] * data["Action"]
print(data)

print("-----")
data['MarketEquity'] = (1 + data['MarketRet']).cumprod()
data['StratEquity']  = (1 + data['StratRet']).cumprod()
print(data)

print("-----")
print(data["MarketEquity"])
print(data["StratEquity"])

print("-----")

