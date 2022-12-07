"""
You need to authenticate with credentials if you want to do anything on GCP.
This is basically like a login step for your code to login on your behalf. 
"""

from dotenv import load_dotenv
import os
import logging

from pydata_google_auth import load_user_credentials, get_user_credentials


def get_credentials():
    """
    This method gets credentials trying two ways in this order:
    1. Load credentials from an environment variable 
        (this is best for local development)
    2. Load credentials from a google-credentials.json file 
        in the same directory.
        (back-up for local development - not recommended.)

    This will return None if the two ways above fail. 
    You want this if you are running code on GCP with a service account 
    or something like that because it will already be authenticated.
    """

    try:
        load_dotenv()
        creds = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        credentials = load_user_credentials(creds)
        logging.info("Nice! Retrieved credentials from local environment.")
    
    except Exception:
        try:
            logging.info("Uh oh...failed to get credentials from local environment.")
            credentials = load_user_credentials("google-credentials.json")
            logging.info("Got credentials from google-credentials.json in local directory.")
        except Exception:
            logging.info("No local credentials found. Hopefully your service account is running this.")
            credentials = None
    
    return credentials


def get_credentials_via_direct_login():
    """
    This method uses the pydata_google_auth method that requests you to login via a browser.
    This is not the advised way but can work in a pinch. 
    """

    try:
        credentials = get_user_credentials(["https://www.googleapis.com/auth/cloud-platform"],)
        logging.info("Getting user credentials via direct login popup.")
    except Exception as e:
        logging.error(f"Unable to get credentials via the pydata_google_auth direct login method: {e}")

    return credentials




