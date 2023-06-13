import pandas as pd
import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1'
response = requests.get(url)

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all div elements with the specified class
div_elements = soup.find_all('div',
                             class_='s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-include-content-margin puis puis-v3gpyfwsnoypgd232yfieockiop s-latency-cf-section s-card-border')

# Initialize lists to store the extracted data
product_urls = []
names = []
prices = []
ratings = []
reviews = []

# Extract the desired information from each div element
for div in div_elements:
    product_url_a = div.find('a',
                             class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    name_span = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    price_span = div.find('span', class_='a-price-whole')
    rating_i = div.find('span', class_='a-icon-alt')
    reviews_span = div.find('span', class_='a-size-base s-underline-text')

    # Store the extracted data in respective lists
    product_urls.append(product_url_a['href'] if product_url_a else '')
    names.append(name_span.text.strip() if name_span else '')
    prices.append(price_span.text.strip() if price_span else '')
    ratings.append(rating_i.text.strip() if rating_i else '')
    reviews.append(reviews_span.text.strip() if reviews_span else '')

# Create a DataFrame to store the data
data = {'Product_URL': product_urls, 'Names': names, 'Price': prices, 'Rating': ratings, 'Reviews': reviews}
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('webscrap.xlsx', index=False)
