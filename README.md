**TOPIC** : _Stock correlation heatmap_

**TEAM MEMBERS**:

Patel Krish Prakashkumar [ku2407u825]

Vipul singh Adhikari [ku2407u735]


**OBJECTIUE OF THE PROJECT :**

Manage Risk: Diversify portfolios and hedge against losses.

Make Informed Decisions: Identify investment opportunities and evaluate portfolio performance.

Analyze Market Dynamics: Understand market trends and predict future movements.

Learn and Grow: Educate users about correlation concepts and improve investment knowledge.

**Tools and Libraries used** : [VS code, pandas, yfinance, seaborn, matplotlib.pyplot, numpy]

**DATA SOURCE :**

YOUTUBE, WIKIPEDIA, CHAT GPT, CLAUDE AI, GEMINI AI

**EXECUTION STEPS :**


_Start the program_ : The script starts by printing a message "Stock Correlation and Visualization Tool".

_Show available companie_s : It displays a list of 16 companies for which you can analyze correlations and stock price movements.

_Get user input_ : It prompts you to enter at least 2 company names separated by commas.

_Validate input :_ The program checks if you entered at least 2 companies and if they are from the available list. It displays error messages if the input is invalid and prompts you to try again.

_Fetch stock data :_ Once you provide valid company names, the program uses the fetch_stock_data function to download historical adjusted closing prices for those companies from Yahoo Finance. By default, it retrieves data from January 1st, 2023 to January 1st, 2024.

_Calculate correlation :_ The create_correlation_heatmap function calculates the correlation coefficient between the stock price changes (percentage changes) for all chosen companies. It then creates a heatmap visualization using a blue color gradient, where darker shades indicate stronger correlations (positive or negative). The heatmap is displayed along with a title "Stock Price Correlation Heatmap".

_Print correlation matrix :_ The program also prints the actual correlation matrix as a table with numbers, allowing you to see the precise correlation values between each pair of stocks.

_Generate candlestick charts_ : Finally, the create_candlestick_charts function generates individual candlestick charts for each selected company. These charts visualize the daily stock price movements along with green triangles indicating positive price changes and red inverted triangles indicating negative changes.

**SUMMARY**

This script provides a simple but powerful way to visualize and analyze stock price correlations. By comparing stock movements between various companies, users can gain insights into how different companies are related in terms of their stock price behavior. This can be useful for making informed investment decisions or understanding market trends.

**CHALLENGES FACED :**

Challenges in Creating Stock Correlation Heatmaps

Data Quality and Availability: Missing or inaccurate data can lead to unreliable results.

Market Volatility and Noise: Short-term fluctuations and external factors can mask underlying relationships.

Correlation vs. Causation: Correlation doesn't imply causation.


Time Frame and Data Frequency: The choice of time frame and data frequency can impact results.

Statistical Limitations: Correlation coefficients may have limitations.

To address these challenges, consider data cleaning, multiple correlation measures, visualization, and cautious interpretation.
