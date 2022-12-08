# Create Client

import os
import logging
from google.cloud import bigquery

from gcp_utils.authentication.credentials import get_credentials


# In order to enable the connection locally or on the cloud we must test to see where we are
# In the GCP environment the 'GCP_PROJECT' environment variable is preset. 
# If you are running locally it will be set to 'None'
try:
    project_id = os.environ.get('GCP_PROJECT')
except Exception:
    logging.error("Failed to test if local environment or GCP environment.")
    raise EnvironmentError("Failed to test if local environment or GCP environment.")


if project_id == None:
    logging.info("Code is running in a local environment (not on GCP). Please specify project_id.")
    def get_client(project_id: str):
        """
        Method to get client when things are local.
        project_id - needs to be specified by user
        """
        client = bigquery.Client(project = project_id, credentials = get_credentials())
        
        return client
else:
    logging.info(f"Code is running in GCP in this project: {project_id}.")

    def get_client():
        """
        Method to get client when things are on GCP.
        project_id - can be inferred
        """
        client = bigquery.Client()
        
        return client




