# Stock-Data-Candlestick-Chart
<p>This project visualizes the stock price data of any specified ticker symbol using candlestick charts. The application leverages the <code>yfinance</code> library to fetch historical stock data and the <code>mplfinance</code> library to create the candlestick charts. This tool is particularly useful for analyzing stock price movements over a specified period.</p>


<p>Here's a brief breakdown of the program:</p>
<b>Data Fetching</b>: Efficiently fetches historical stock data using the <code>yfinance</code> library.
<b>Data Preparation</b>: Processes the data to be compatible with the candlestick chart format.
<b>Visualization</b>: Creates a visually appealing candlestick chart using <code>mplfinance</code>.
<b>Customization</b>: Provides options to customize the chart's appearance, such as background color and title.


### Install the Package
pip install yfinance mplfinance
<p>In the terminal of the Python environment.</p>


### Usage
<p>1. <b>Run the Application</b>:</p>
<pre><code>python candlestick_chart.py</code></pre>
<p>2. <b>Specify Details</b>:</p>
<ul>
    <li>Modify the <code>ticker</code> variable in the script to the desired stock ticker symbol (e.g., 'AAPL' for Apple Inc.).</li>
    <li>Adjust the <code>start</code> and <code>end</code> variables to set the time frame for the data.</li>
</ul>
<p>3. <b>View Chart</b>:</p>
<ul>
    <li>The script will generate a candlestick chart for the specified stock and display it.</li>
</ul

### Contributor
<p>Lawrence Menegus</p>
