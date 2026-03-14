import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TechnicalAnalysis:
    def __init__(self, data):
        self.data = data

    def moving_average(self, window):
        return self.data['Close'].rolling(window=window).mean()

    def rsi(self, period=14):
        delta = self.data['Close'].diff()  
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()  
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def macd(self, short_window=12, long_window=26, signal_window=9):
        short_ema = self.data['Close'].ewm(span=short_window, adjust=False).mean()
        long_ema = self.data['Close'].ewm(span=long_window, adjust=False).mean()
        macd = short_ema - long_ema
        signal_line = macd.ewm(span=signal_window, adjust=False).mean()
        return macd, signal_line

    def bollinger_bands(self, window=20, num_sd=2):
        rolling_mean = self.data['Close'].rolling(window).mean()
        rolling_std = self.data['Close'].rolling(window).std()
        upper_band = rolling_mean + (rolling_std * num_sd)
        lower_band = rolling_mean - (rolling_std * num_sd)
        return upper_band, lower_band

    def plot_indicators(self):
        plt.figure(figsize=(15,10))
        plt.plot(self.data['Close'], label='Close Price', color='blue', alpha=0.5)

        ma50 = self.moving_average(50)
        ma200 = self.moving_average(200)
        plt.plot(ma50, label='50-Day Moving Average', color='orange')
        plt.plot(ma200, label='200-Day Moving Average', color='green')

        rsi = self.rsi()
        plt.figure()
        plt.plot(rsi, label='RSI', color='purple')
        plt.axhline(70, linestyle='--', alpha=0.5, color='red')
        plt.axhline(30, linestyle='--', alpha=0.5, color='green')

        macd, signal = self.macd()
        plt.figure()
        plt.plot(macd, label='MACD', color='blue')
        plt.plot(signal, label='Signal Line', color='red')

        upper_band, lower_band = self.bollinger_bands()
        plt.plot(upper_band, label='Upper Band', color='red')
        plt.plot(lower_band, label='Lower Band', color='red')
        plt.fill_between(self.data.index, lower_band, upper_band, color='red', alpha=0.1)

        plt.legend()
        plt.show()