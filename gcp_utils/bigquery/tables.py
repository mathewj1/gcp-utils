# This class enables object-oriented access to a Google Big Query Table
import logging
from gcp_utils.bigquery import get_client
from google.api_core.exceptions import NotFound

class Table:
    def __init__(self, table_id: str):
        self.table_id = table_id
    
    def table_exists(self):
        """
        Check if table exists. 
        table_id = "your-project.your_dataset.your_table"
        """

        client = get_client()

        try:
            client.get_table(self.table_id)  # Make an API request.
            logging.info(f"Table {self.table_id} exists.")
            return True
        except NotFound:
            logging.info(f"Table {self.table_id} is not found.") 
            return False


    
