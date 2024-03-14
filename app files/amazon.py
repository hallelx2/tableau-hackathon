from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

import re
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

def build_amazon_search_url(search_param):
    base_url = "https://www.amazon.com/s"
    search_query = {"k": search_param}
    url = base_url + "?" + "&".join([f"{key}={value}" for key, value in search_query.items()])
    return url

def build_amazon_page_search(search_param, page=1):
    base_url = "https://www.amazon.com/s"
    search_query = {"k": search_param.replace(" ", "+"), "page": page}
    url = base_url + "?" + "&".join([f"{key}={value}" for key, value in search_query.items()])
    return url

def create_data_set(product_desc: list, prices: list) -> dict:
    """
    Creates a dictionary named 'data_set' containing product descriptions and prices as separate lists,
    ensuring both lists have the same size.

    Args:
        product_desc (list): A list of product descriptions.
        prices (list): A list of corresponding prices.

    Returns:
        dict: A dictionary named 'data_set' with keys 'Product Description' and 'Prices'. The shorter
              list is used to determine the final dataset size.

    """

    
    # Ensure both lists have the same size by selecting the minimum length
    data_set_size = min(len(product_desc), len(prices))

    # Select elements from the longer list up to the data_set_size
    product_desc_subset = product_desc[:data_set_size]
    prices_subset = prices[:data_set_size]

    data_set = {
        'Product Description': product_desc_subset,
        'Prices': prices_subset
    }

    return data_set

def scrape_amazon(search_param, number_of_pages=5):
    
    # instantiate a browser object
    browser = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
    
    # Build a URL for search and get the page
    website = build_amazon_search_url(search_param)
    browser.get(website)
    
    # Identifiers for the objects to be Scraped
    prod_class = "span.a-color-base.a-text-normal"
    price_class = "span.a-price-whole"
    rating_class = "a-size-mini"
    
    
    # Instantiate the items to be scraped
    product_desc = []
    prices = []
    ratings = []
    
    # Scrape per page
    for i in range(number_of_pages):
        i+=1
        
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # Scroll to bottom

        # Find elements for product information on the current page
        products = browser.find_elements(By.CSS_SELECTOR, prod_class)
        price = browser.find_elements(By.CSS_SELECTOR, price_class)
        # rating = browser.find_elements(By.CSS_SELECTOR, rating_class)
        
        # Extract product information from each product
        for j in range(len(products)):
           try:
               product_desc.append(products[j].text)
               prices.append(float(price[j].text))
               # ratings.append(rating[j].text)
           except:
               pass
        
        # Navigate to the next page
        browser.get(build_amazon_page_search(website, i))
        sleep(10)
    
    
    # Create and return the DataFrame
    data_set = create_data_set(product_desc, prices)
    
    df = pd.DataFrame(data_set)
    return df