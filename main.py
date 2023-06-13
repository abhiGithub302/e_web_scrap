import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML file
with open('aaa.html', 'r') as file:
    html_content = file.read()

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with the specified class
div_elements = soup.find_all('div',
                             class_='s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-include-content-margin puis puis-v3gpyfwsnoypgd232yfieockiop s-latency-cf-section s-card-border')

# Initialize lists to store the extracted data
names = []
prices = []
reviews = []

# Extract the desired information from each div element
for div in div_elements:
    name_span = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    price_span = div.find('span', class_='a-price-whole')
    reviews_span = div.find('span', class_='a-icon-alt')

    # Store the extracted data in respective lists
    names.append(name_span.text.strip() if name_span else '')
    prices.append(price_span.text.strip() if price_span else '')
    reviews.append(reviews_span.text.strip() if reviews_span else '')

# Create a DataFrame to store the data
data = {'Names': names, 'Price': prices, 'Reviews': reviews}
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
