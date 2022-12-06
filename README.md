# gcp-utils
A set of methods to help me leverage Google Cloud Platform in my projects


##Authentication 

The authentication module handles the authentication to GCP in case you are running code locally. 
To authenticate locally I have found two ways: 
**BE SURE TO INCLUDE YOUR CREDENTIAL FILE IN YOUR .gitignore FILE.... god forbid you commit/publish that and let some rando access your GCP instance**
1. Set Environment Variable
    This method requires you to set up a *.env* in your directory with the following path to your credentials file:
    ```
    #Google Credentials
    GOOGLE_APPLICATION_CREDENTIALS=YOUR/PATH/TO/FILE/google-credentials.json
    ```
2. Place Credentials File in Directory
    If you place your credentials file in the authentiction module directory, whenever you call the function, it should be able to find it. Just be sure to call it *google-credentials.json*.

How do you get this file in the first place?
https://developers.google.com/workspace/guides/create-credentials
NEED TO ADD MORE DETAILS HEER

Another way you can authenticate is by requesting a direct login pop-up. Basically enabling you to login to your Google Workspace from the browser. You must call the `get_credentials_via_direct_login()` method.
  