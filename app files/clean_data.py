import pandas as pd
import re

def create_data_set(product_descriptions: list, prices: list, shipping_prices: list = None, store_names: list = None) -> dict:
    """
    Creates a dictionary named 'data_set' containing product descriptions, prices,
    optional shipping prices, and optional store names extracted from multiple products.

    Args:
        product_descriptions (list): A list of product descriptions.
        prices (list): A corresponding list of prices.
        shipping_prices (list, optional): A list of corresponding shipping prices. Defaults to None.
        store_names (list, optional): A list of corresponding store names. Defaults to None.

    Returns:
        dict: A dictionary named 'data_set' with keys:
            - 'Product Description': List of product descriptions.
            - 'Prices': List of corresponding prices.
            - 'Shipping Prices' (optional): List of corresponding shipping prices if provided.
            - 'Store Names' (optional): List of corresponding store names if provided.

    Raises:
        ValueError: If the lengths of any two lists do not match, indicating inconsistent data.
    """

    # Ensure all lists have the same length
    min_length = min(len(product_descriptions), len(prices), len(shipping_prices), len(store_names))

    # Select elements from longer lists up to the minimum length
    product_desc_subset = product_descriptions[:min_length]
    prices_subset = prices[:min_length]
    shipping_subset = shipping_prices[:min_length]
    store_names_subset = store_names[:min_length]

    data_set = {
        'Product Description': product_desc_subset,
        'Prices': prices_subset,
        'Shipping Prices': shipping_subset,
        'Store Names': store_names_subset
    }

    return data_set


def clean_alibaba(df):
    # Remove 'NGN' and comma from price and convert to float
    def clean_price(price):
        cleaned_price = price.replace('NGN', '').replace(',', '')
        return float(cleaned_price)

    
    # Clean shipping fee column
    def clean_shipping_fee(shipping_fee):
        if shipping_fee == 'Free shipping':
            return 0.0
        elif '+Shipping' in shipping_fee:
            # Extracting the price from the string using regular expression
            price_match = re.search(r'NGN([\d,]+\.\d+)', shipping_fee)
            if price_match:
                return float(price_match.group(1).replace(',', ''))
        else:
            return None
    
    df["Shipping Prices"] = df["Shipping Prices"].apply(clean_shipping_fee)
    df['Prices'] = df['Prices'].apply(clean_price)
    
    return df
