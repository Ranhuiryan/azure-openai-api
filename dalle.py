import requests
import time
import importlib

# import variables "AZURE_OPENAI_API_KEY", "AZURE_OPENAI_API_ENDPOINT" from config.py
api_key = getattr(importlib.import_module("config_private"), "AZURE_OPENAI_API_KEY")
api_base = getattr(importlib.import_module("config_private"), "AZURE_OPENAI_API_ENDPOINT")
api_version = '2023-06-01-preview'
url = "{}openai/images/generations:submit?api-version={}".format(api_base, api_version)
headers= { "api-key": api_key, "Content-Type": "application/json" }
body = {
    "prompt": "The seattle skyline and space needle, impressionist painting",
    "n": 2,
    # "resolution": "1024x1024"
}
submission = requests.post(url, headers=headers, json=body)
operation_location = submission.headers['Operation-Location']
status = ""
while (status != "succeeded"):
    time.sleep(3)
    response = requests.get(operation_location, headers=headers)
    status = response.json()['status']
for data in response.json()['result']['data']:
    image_url = data['url']
    print(image_url)
# image_url = response.json()['result']['contentUrl']