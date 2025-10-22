# Author: Sanan Alam
# Date: October 2025
# Tracks S&P 500 growth over time using Python, yfinance, and matplotlib

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_sp500_history(period="5y"):
    """Fetch historical data for the S&P 500"""
    try:
        sp500 = yf.Ticker("^GSPC")
        # use a daily interval explicitly
        hist = sp500.history(period=period, interval="1d")
        if hist is None or hist.empty:
            print("Hmm, no data returned. Check network, ticker, or period.")
            return None
        return hist
    except Exception as e:
        print("Something went wrong fetching data:", e)
        return None

def add_growth_column(df):
    """Calculate percent growth from the first day"""
    start = df['Close'].iloc[0]
    df['GrowthPct'] = (df['Close'] - start) / start * 100
    return start, df

def plot_growth(df):
    """Make a simple line chart of growth"""
    plt.figure(figsize=(10,6))
    plt.plot(df.index, df['GrowthPct'], color='green', linewidth=2)
    plt.title("S&P 500 Growth Over Time")
    plt.xlabel("Date")
    plt.ylabel("Growth (%)")
    plt.grid(True)
    plt.show()

def main():
    period = (input("How far back do you want to track? (1y, 5y, max) ") or "5y").strip().lower()
    # small whitelist of commonly used valid period strings
    valid_periods = {"1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"}
    if period not in valid_periods:
        print(f"Period '{period}' not recognized. Using default '5y'. Valid examples: 1y, 5y, max")
        period = "5y"

    data = get_sp500_history(period)

    if data is not None:
        start_price, data = add_growth_column(data)
        plot_growth(data)

        latest = data['Close'].iloc[-1]
        total_growth = data['GrowthPct'].iloc[-1]
        print(f"Start Price: ${start_price:.2f}")
        print(f"Latest Price: ${latest:.2f}")
        print(f"Total Growth: {total_growth:.2f}%")
        print("\nDone! Pretty cool to see how the S&P has changed, right?")

if __name__ == "__main__":
    main()
