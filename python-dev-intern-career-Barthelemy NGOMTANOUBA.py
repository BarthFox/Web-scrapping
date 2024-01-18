import requests
from bs4 import BeautifulSoup
import pandas as pd

# Specify the URL of the website
url = "https://www.jumia.sn/"
# Send a GET request to the URL
response = requests.get(url)
# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data based on HTML structure
products = soup.find_all('article', class_='prd _box _hvr')

# Initialize lists to store data
product_name = []
products_price = []
discount = []

# Extract product details
for product in products:
    # Extract product name
    name_element = product.find('h2', class_='title')
    product_name.append(name_element.text.strip() if name_element else '')

    # Extract product price
    price_element = product.find('div', class_='prc')
    products_price.append(price_element.text.strip() if price_element else '')

    # Extract discount
    discount_element = product.find('div', class_='bdg _dsct')
    discount.append(discount_element.text.strip() if discount_element else '')

# Create a DataFrame
df = pd.DataFrame({
    "Product name": product_name,
    "Product price": products_price,
    "Discount": discount
})

# Print and save the DataFrame to a CSV file
print(df)
df.to_csv("jumia_ci.csv", index=False, encoding='utf-8')
