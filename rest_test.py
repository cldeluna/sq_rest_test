#!/usr/bin/python -tt
# Project: rest_test
# Filename: rest_test.py
# claudia
# PyCharm

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "3/26/2025"
__copyright__ = "Copyright (c) 2025 Claudia"
__license__ = "Python"


import os
import dotenv
import requests


def try_sq_rest_call(uri_path, url_options, API_ENDPOINT="suzieq.uwaco.net"):
    """
    SuzieQ API REST Call

    """

    API_ACCESS_TOKEN = os.getenv("SQ_API_TOKEN")

    url = f"https://{API_ENDPOINT}:8443{uri_path}?{url_options}"
    # UWACO LAB
    # url = f"https://{API_ENDPOINT}:8443{uri_path}?{url_options}"
    payload = "\r\n"
    headers = {
        "Content-Type": "text/plain",
        "Authorization": f"Bearer {API_ACCESS_TOKEN}",
    }

    # Send API request
    try:
        response = requests.get(url, headers=headers, data=payload, verify=False)
    except Exception as e:
        response = False

    # Returns full response object
    return response



def get_namespace_list():
    # Initialize
    namespace_list = list()

    # Trick to get a unique list of namespaces for the pull down
    URI_PATH = "/api/v2/device/unique"
    URL_OPTIONS = f"columns=namespace&ignore_neverpoll=true"
    ns_response = try_sq_rest_call(URI_PATH, URL_OPTIONS, API_ENDPOINT="mysuzieqserver")

    # Create a list of namespaces from the list of dictionaries
    if ns_response:
        if ns_response.status_code == 200:
            if ns_response.json():
                namespace_list = [line["namespace"] for line in ns_response.json()]
    else:
        print("Error")
        exit()

    return namespace_list


def main():

    # Load the SuzieQ API Key from Environment Variable

    dotenv.load_dotenv()

    # Test to make sure TOKEN is in an Environment Variable
    if not os.getenv("SQ_API_TOKEN"):
        print(
            "SuzieQ Token cannot be found in an environment variable. "
            "Make sure your .env_sample file has been updated with a valid Bearer Token for the SuzieQ REST API!"
        )

    nslist = get_namespace_list()
    print(nslist)



# Standard call to the main() function.
if __name__ == "__main__":
    main()