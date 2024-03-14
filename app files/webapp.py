import streamlit as st
import pandas as pd

# Import scraper and Tableau functions (from previous sections)
from amazon import scrape_amazon
from alibaba import scrape_aliexpress
from hyper import dataframe_to_hyper
from publish import publish_hyper


def main():
    st.title('Marketeer')
    st.write("""
            Streamlit app for scraping product data and publishing to Tableau
            This will help businesses make analysis quickly and it expands the options that they get to have.

             
            Take your businesses to the next level. With Marketeer, you can take your market analysis from here to there.
    """)

    # Sidebar options
    source_options = ["Amazon", "AliExpress"]
    source = st.sidebar.selectbox("Choose Source", source_options)
    product_name = st.sidebar.text_input("Product Name")
    num_pages = st.sidebar.slider('Number of Pages', 1, 10)

    # Scrape button
    if st.sidebar.button("Scrape Data"):
        if source == "Amazon":
            df = scrape_amazon(product_name)
            st.progress(1.0)  # Update progress bar to 100%
        elif source == "AliExpress":
            df = scrape_aliexpress(product_name)
        else:
            st.error("Invalid source selection")
            return

        # Display scraped data (ensure all data is shown)
        st.header("Scraped Data")
        st.write(df)  # Display the entire DataFrame

    with st.button('Publish'):
        # Tableau publishing options
        hyper_name = dataframe_to_hyper(df)
        tableau_server_address = st.text_input("Tableau Server Address")
        tableau_site_name = st.text_input("Tableau Site Name")
        tableau_token_name = st.text_input("Tableau Token Name")
        tableau_token_value = st.text_input('Tableau Token Value', type = 'password')
        publish_hyper(hyper_name, tableau_server_address, tableau_site_name, tableau_token_name, tableau_token_value, project_name='default')


if __name__=='__main__':
    main()
