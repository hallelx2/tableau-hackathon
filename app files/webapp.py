import os
import streamlit as st
from pathlib import Path  # For file path handling


from publish import publish_hyper
from alibaba import scrape_aliexpress
from amazon import scrape_amazon
from hyper import dataframe_to_hyper


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # For visualizations (optional)

# Set page title and icon
st.set_page_config(page_title="Marketeer: Scrape & Publish to Tableau", page_icon="")

# Header with Marketeer logo (replace with your logo image)
st.header("Marketeer", "")
st.image("marketeer_logo.png", width=500)  # Replace with your logo path

# Description with a sidebar layout
st.sidebar.title("Scrape & Visualize Data")
st.sidebar.write("Effortlessly collect product data and gain insights before publishing to Tableau.")

# Input fields in the main content area
source_select = st.selectbox("Select Data Source", ["Amazon", "AliExpress"])
search_param = st.text_input("Search Term for Products")
pages = st.number_input("Number of Pages to Scrape (Optional)", min_value=1)

# Tableau Server details (placeholders if not using API)
st.sidebar.title("Tableau Details")
server_address_input = st.sidebar.text_input("Tableau Server/Online Address", value="https://10ax.online.tableau.com")
site_name_input = st.sidebar.text_input("Tableau Site Name")
token_name_input = st.sidebar.text_input("Personal Access Token Name")
token_value_input = st.sidebar.text_input("Personal Access Token Value", type="password")
project_name_input = st.sidebar.text_input("Tableau Project Name", value = "default")

current_dir = os.path.dirname(os.path.abspath(__file__))

# Button and processing
if st.button("Scrape, Visualize & Publish"):
    # Basic validation (assuming validation is done in your API)
    if not search_param:
        st.error("Please enter a search term.")

    # Disable button while processing and show spinner
    with st.spinner("Scraping, Visualizing, & Publishing..."):
        # Simulate scraping data
        if source_select == "Amazon":
            st.info("Scraping product data from Amazon...")
            hyper_res = scrape_amazon(search_param)  # Replace with actual implementation
            hyper_path = dataframe_to_hyper(hyper_res, f'{search_param} amazon.hyper')
            hyper_name = os.path.join(current_dir, hyper_path)
        elif source_select == "AliExpress":
            st.info("Scraping product data from AliExpress...")
            hyper_res = scrape_aliexpress(search_param)  # Replace with actual implementation
            hyper_path = dataframe_to_hyper(hyper_res, f'{search_param} aliexpress.hyper')
            hyper_name = os.path.join(current_dir, hyper_path)


        # Convert scraped data to DataFrame
        df = pd.DataFrame(hyper_res)

        # Sort by price in descending order and get the top 10 most expensive products
        df = df.sort_values(by='Prices', ascending=False).head(10)

        # Display some basic data exploration (optional)
        st.subheader("Data Exploration")
        st.write(df.head())  # Show the first few rows
        st.write(df.describe())  # Summary statistics

        # Visualizations section (optional)
        st.subheader("Data Visualizations")
        col1, col2 = st.columns(2)  # Create two columns for visualizations

        # Example visualizations (replace with your desired charts)
        with col1:
            fig, ax = plt.subplots()
            sns.barplot(x="Product Description", y="Prices", data=df)  # Bar plot for top expensive products
            ax.set_title("Top 10 Most Expensive Products")
            # Truncate long product descriptions for better readability (optional)
            plt.xticks(rotation=45, ha='right')  # Rotate and right-align x-axis labels
            st.pyplot(fig)

        with col2:
            fig, ax = plt.subplots()
            sns.boxplot(x="Product Description", y="Prices", data=df)  # Box plot by category (optional)
            ax.set_title("Price Distribution by Category (Top 10)")
            # Truncate long product descriptions for better readability (optional)
            plt.xticks(rotation=45, ha='right')  # Rotate and right-align x-axis labels
            st.pyplot(fig)

        # Generate Hyper file (assuming `dataframe_to_hyper` works)
        hyper_path = dataframe_to_hyper(df, f'{search_param}.hyper')

        # Publish to Tableau (assuming `publish_hyper` works)
        publish_hyper(
            Path(hyper_path),
            server_address_input,
            site_name_input,
            token_name_input,
            token_value_input,
            project_name_input,
        )

        st.success("Data scraped, visualized, and published successfully!")
