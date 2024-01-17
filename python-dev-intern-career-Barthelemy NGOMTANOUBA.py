#Website scrapped : https://www.jumia.ci/
#We will scrap most popular product 
#Offers of the week
#Best offers
#Best Categories
#Best offers | Up to 60% off
#Best offers | Up to 70% off

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Specify the URL of the website
url = "https://www.jumia.ci/"
# Send a GET request to the URL
response = requests.get(url)
# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')
        
# Extract data based on HTML structure
headlines = soup.find_all('h2', class_='-m -fs20 -elli')
products = soup.find_all('article', class_='prd _box _hvr')


# Initialize lists to store data
product_name = []
products_price = []
prices_list = []
discount = []

 # Extract product details
for product in products:
    product_name.append(product.getText())
    products_price.append(product.getText())
    discount.append(product.getText())
    
    df = pd.DataFrame.from_dict( {"Product name" : product_name, "Product price" : products_price, "Discount" : discount})
    print(df)
    # Function to store data in a CSV file using Pandas
    df.to_csv("jumia_ci.csv", index=False, encoding ='utf-8')

    #product_info = {
    #    'Name': product.find('div', class_='name').text.strip(),
    #    'Price': product.find('div', class_='prc').text.strip(),
    #    'Discount': product.find('div', class_='bdg _dsct').text.strip(),
        #'Link': product.find('a')['href']
    #}
   
    
