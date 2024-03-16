## Marketeer: A Web API and App for Data-Driven Market Insights


**Inspiration**

In today's competitive business landscape, data-driven decision making is crucial for success. However, technical expertise for data analysis can be a barrier for many business owners. Marketeer aims to bridge this gap by providing a web application that empowers both businesses and individual consumers to gain market insights and make informed choices.

**Problem**

- Difficulty for business owners to track competitor pricing and optimize their own pricing strategies.
- Challenges for consumers to find the best deals online amidst varying product prices.

**Solution**

Marketeer is a web application designed to:

1. **Gather product data:** Scrapes data on user-specified goods from various e-commerce websites (e.g., Amazon, AliExpress).
2. **Clean and analyze data:** Cleans and processes the scraped data to generate valuable insights. Automatically creates hyper files that are uploaded to the tableau online or server where further analysis can be done.
3. **Visualize trends:** Presents data in clear and actionable visualizations using python, and extend by doing personalised analysis in your tableau online or server using the hyper database.
4. **Personalized dashboards:** Offers customizable dashboards for individual users or team collaborations. (coming)
5. **API Access:** A public API to allow developers to integrate Marketeer's data gathering and analysis functionalities into their own applications.

**Technology Stack**

- **Data Scraping:** Selenium
- **Data Cleaning:** Pandas
- **Data Connectivity:** Tableau Server Client library, Hyper API, Pantab
- **Web API Development:** FastAPI
- **Frontend Interactivity:** Python Streamlit

**Challenges**

1. **Website Structure:** Understanding website structures and navigating popups. (Solution: Executing JavaScript functions within Selenium)
2. **Data Consistency:** Ensuring consistent data volume across scraping runs. (Potential cause: Website connectivity and dynamic content loading)
3. **Search Relevance:** Balancing data quantity with search relevance. (Focusing on the first two pages of search results for optimal accuracy)

## Accomplishments We're Proud Of

We're thrilled to announce the successful launch of Marketeer! Here are some of our key achievements:

Developed APIs for this purpose that can then be further used by programmers seeking to extend their capability, hence we offer flexibility. For our non-tech users, we have a simple streamlit webapp that automates the process for you. This will empowers users with market insights.

Integrated industry-leading data scraping and visualization tools for comprehensive analysis.
Built a scalable and robust architecture to handle various data volumes and user demands.

## What's Next for Marketeer

We're constantly innovating and expanding Marketeer's capabilities. Here's a glimpse into the future:

- **Global Expansion:** Integrate support for additional e-commerce websites, catering to a wider international audience.
- **Advanced Analytics Features:** Implement machine learning algorithms, natural language processing, and more integrations to provide predictive insights and identify future market trends.
- **Customisable Alerts:** Allow users to set up price alerts for specific products and receive notifications when prices change.
- **Integration of More APIs:** COnnect more APIs to ensure greater connectivity for the users


We believe Marketeer has the potential to revolutionise the way businesses and consumers approach market research. By providing easy-to-use data analysis tools, Marketeer empowers informed decision-making and levels the playing field for everyone.

Join us on our journey to unlock the power of market data, using the prowess of **Tableau APIs**!

## Usage
Requirements: Python, chrome browser, pip or pipenv, tableau onlline account

- Use ```pipenv sync``` to activate the virtual environment
- Navigate to the ```app files``` direectory to  run the streamlit app and also the API
- To deploy the API, run ```uvicorn api:app --reload```. THis opens up a swagger documentation in your browser which you can interact with
- Run ```streamlit run webapp.py``` to be able to ineract with the front end.
- The hyper files get sent to your tableau depending on the api you chose. Now you can visit tableau to continue your analysis

