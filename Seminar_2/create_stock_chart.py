import matplotlib.pyplot as plt
import yfinance as yf

# Function to create a stock chart for a given stock between two dates and return the chart
def create_stock_chart(stock, start_date, end_date):
    # Get the stock data
    stock_data = yf.download(stock, start=start_date, end=end_date)
    # Create the stock chart
    # Create the stock chart
    fig, ax = plt.subplots(figsize=(12, 6))  # Create a figure and axis
    ax.plot(stock_data['Close'], label=stock)
    ax.set_title(f'{stock} Stock Chart')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid()

    # Save the chart as a PNG file
    fig.savefig(f'{stock}_stock_chart.png')
    
    # close the plot
    plt.close(fig)

    # Return the file path of the saved chart
    return f'{stock}_stock_chart.png'

