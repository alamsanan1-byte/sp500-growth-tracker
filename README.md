S&P 500 Growth Tracker

Author: Sanan Alam  


This Python project tracks the historical growth of the S&P 500 index and visualizes it as a percentage change
over time.
It uses **yfinance** to fetch real-time data, **pandas** for data processing, and **matplotlib** for
visualization.  

  Features
- Fetches historical S&P 500 data (user-selectable period: 1y, 5y, max, etc.)
- Calculates percentage growth from the first day
- Plots growth over time with a clean, interactive chart
- Displays starting price, latest price, and total growth  

Technologies
- Python 3
- yfinance
- pandas
- matplotlib

How to Run
1. Install dependencies:
(Into terminal)

pip install yfinance pandas matplotlib

2. Run the script:

python sp500_tracker.py

3. Enter the period when prompted (e.g., `1y`, `5y`, `max`)
4. View the plotted growth chart and printed summary

 Example Output

Start Price: $3400.50
Latest Price: $4200.75
Total Growth: 23.53%



