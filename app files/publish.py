'''

Snippet inspired by @tsjoblad, github and then modified to suite the need

'''

from pathlib import Path
import tableauserverclient as TSC



def publish_hyper(hyper_name, server_address , site_name, token_name, token_value, project_name):
    """
    Shows how to leverage the Tableau Server Client (TSC) to sign in and publish an extract directly to Tableau Online/Server
    """
    path_to_database = Path(hyper_name)

    # Sign in to server
    tableau_auth = TSC.PersonalAccessTokenAuth(token_name=token_name, personal_access_token=token_value, site_id=site_name)
    server = TSC.Server(server_address, use_server_version=True)

    print(f"Signing into {site_name} at {server_address}")
    with server.auth.sign_in(tableau_auth):
        # Define publish mode - Overwrite, Append, or CreateNew
        publish_mode = TSC.Server.PublishMode.Overwrite

        # Get project_id from project_name
        all_projects, pagination_item = server.projects.get()
        for project in TSC.Pager(server.projects):
            if project.name == project_name:
                project_id = project.id

        # Create the datasource object with the project_id
        datasource = TSC.DatasourceItem(project_id)

        print(f"Publishing {hyper_name} to {project_name}...")
        # Publish datasource
        datasource = server.datasources.publish(datasource, path_to_database, publish_mode)
        print("Datasource published. Datasource ID: {0}".format(datasource.id))
