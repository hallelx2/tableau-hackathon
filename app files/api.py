import os
from fastapi import FastAPI, Query,  Body, Response
from fastapi.responses import JSONResponse, RedirectResponse
import json  # Import the json library
from typing import Optional
import pantab as pt

from alibaba import scrape_aliexpress  # Import the function from alibaba.py
from amazon import scrape_amazon  # Import the scraping function
from hyper import dataframe_to_hyper
from publish import publish_hyper


app = FastAPI()

@app.get("/")
async def root():
    """
    Home route with multiple path operations.
    """
    return RedirectResponse(url="/docs")


@app.get("/scrape-aliexpress")
async def scrape_products(search_term: str = Query(..., description="The product to search for"),
                           num_pages: int = Query(5, description="Number of pages to scrape")):
    
    """Scrapes product data from AliExpress for the given search term.

    Args:
        search_param (str): The product to search for on Amazon.
        number_of_pages (int, optional): Number of pages to scrape (default: 5, minimum: 1).

    Returns:
        dict: An hyper file path containing scraped product to be used in tableau for further analysis
    """
    df = scrape_aliexpress(search_term, num_pages)

    hyper_file = dataframe_to_hyper(df, f'{search_term} aliexpress.hyper')

    return hyper_file

@app.get("/scrape-amazon")
async def scrape_amazon_products(
    search_param: str = Query(..., description="The product to search for on Amazon"),
    number_of_pages: Optional[int] = Query(5, gt=0, description="Number of pages to scrape (default: 5, minimum: 1)"),
):
    """Scrapes product data from Amazon for the given search term.

    Args:
        search_param (str): The product to search for on Amazon.
        number_of_pages (int, optional): Number of pages to scrape (default: 5, minimum: 1).

    Returns:
        dict: An hyper file path containing scraped product to be used in tableau for further analysis

    Raises:
        ValueError: If the number of pages is less than 1.
    """

    if number_of_pages < 1:
        raise ValueError("Number of pages must be at least 1.")

    try:
        df = scrape_amazon(search_param, number_of_pages)
        hyper_file = dataframe_to_hyper(df, f'{search_param} amazon.hyper')
        return hyper_file
    except Exception as e:
        return {"error": str(e)}  # Handle potential scraping errors
    

@app.post("/scrape-and-publish")
async def scrape_and_publish(
    source: str = Query(..., description="Choose 'amazon' or 'aliexpress'"),
    search_param: str = Query(..., description='What would you love to get data on?'),
    pages: int = Query(5, description= 'Number of pages'),
    server_address: str = Query('https://10ax.online.tableau.com', description="Tableau Server address"),
    site_name: str = Query(..., description="Tableau Site Name"),
    token_name: str = Query(..., description="Tableau Token Name"),
    token_value: str = Query(..., description="Tableau Token Value"),
    project_name: str = Query("default", description="Tableau Project Name"),
):
    try:
        # Validate user input
        if source not in ("amazon", "aliexpress"):
            return JSONResponse(status_code=400, content={"error": "Invalid source"})

        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Call the appropriate scraper function
        if source == "amazon":
            hyper_res = scrape_amazon(search_param)  # Replace with actual implementation
            hyper_path = dataframe_to_hyper(hyper_res, f'{search_param} amazon.hyper')
            hyper_name = os.path.join(current_dir, hyper_path)
        elif source == "aliexpress":
            hyper_res = scrape_aliexpress(search_param)  # Replace with actual implementation
            hyper_path = dataframe_to_hyper(hyper_res, f'{search_param} aliexpress.hyper')
            hyper_name = os.path.join(current_dir, hyper_path)

        # Publish the Hyper file to Tableau
        publish_hyper(hyper_name, server_address, site_name, token_name, token_value, project_name)
        os.remove(hyper_name)

        return JSONResponse(content={"message": "Data scraped and published successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
