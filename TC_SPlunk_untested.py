import os
import requests
import datetime
import json

def get_tags_modified_last_180_days(tags):
    # Set up the parameters for the API call
    base_url = "https://api.threatconnect.com"
    api_path = "/v2/tags"

    # Set up the query string parameters
    days = 180
    modified_date = datetime.datetime.utcnow() - datetime.timedelta(days=days)
    query_params = {
        "modifiedSince": modified_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "filter": "tag.name:" + " OR tag.name:".join(tags)
    }

    # Set up the headers for authentication
    access_id = os.environ.get("TC_ACCESS_ID")
    secret_key = os.environ.get("TC_SECRET_KEY")
    if not access_id or not secret_key:
        raise ValueError("TC_ACCESS_ID or TC_SECRET_KEY not found in environment")
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    content_type = "application/json"
    headers = {
        "Timestamp": timestamp,
        "Content-Type": content_type,
        "Authorization": "TC " + access_id + ":" + secret_key
    }

    # Make the API call
    response = requests.get(base_url + api_path, headers=headers, params=query_params)
    response.raise_for_status()

    # Convert the response data to a list of dictionaries
    response_data = response.json()["data"]
    response_dicts = []
    for item in response_data:
        response_dicts.append(item["attribute"])
    return response_dicts

def write_lookup_file(data, filename):
    # Write the response data to a lookup file in Splunk
    with open(filename, "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")
    print(f"Data written to {filename}")

if __name__ == "__main__":
    # Get the tags to search for from the user
    tags = input("Enter the tags to search for (separated by spaces): ").split()

    # Get the lookup file name from the user
    lookup = input("Enter the name of the lookup file to write to: ")

    # Get the last 180 days of data from ThreatConnect
    try:
        response_dicts = get_tags_modified_last_180_days(tags)
    except Exception as e:
        print("Error getting data from ThreatConnect:", e)
        exit(1)

    # Write the data to a lookup file in Splunk
    try:
        write_lookup_file(response_dicts, lookup)
    except Exception as e:
        print("Error writing data to lookup file:", e)
        exit(1)
