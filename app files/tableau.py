import tableauserverclient as TSC
import tableaudocumentapi as TDA
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_NAME = os.getenv('TOKEN_NAME')
TOKEN_VALUE = os.getenv('TOKEN_VALUE')
SITENAME = os.getenv('SITENAME')
SERVER_URL = 'https://10ax.online.tableau.com'

tableau_auth = TSC.PersonalAccessTokenAuth(TOKEN_NAME, TOKEN_VALUE, SITENAME)
server = TSC.Server(SERVER_URL, use_server_version=True)


with server.auth.sign_in(tableau_auth):
    all_workbooks, pagination_item = server.projects.get()
    print("\nThere are {} workbooks on site: ".format(pagination_item.total_available))
    print([workbook.name for workbook in all_workbooks])


def create_new_workbook(TOKEN_NAME, TOKEN_VALUE, SITENAME, SERVER_URL = 'https://10ax.online.tableau.com'):
    pass

def add_data(df):
    pass

def retrieve_graphs():
    pass