import yfinance as yf


ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2025-01-01')
print(data.info())
print(data.head())

print("-----")
print(type(data))


