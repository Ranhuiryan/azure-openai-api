import requests
import time
import importlib

# import variables "AZURE_OPENAI_API_KEY", "AZURE_OPENAI_API_ENDPOINT" from config.py
api_key = getattr(importlib.import_module("config_private"), "AZURE_OPENAI_API_KEY")
api_base = getattr(importlib.import_module("config_private"), "AZURE_OPENAI_API_ENDPOINT")
deployment_id = getattr(importlib.import_module("config_private"), "AZURE_OPENAI_API_DEPLOYMENT_ID")
stream = False

api_version = '2023-05-15'
url = "{}openai/deployments/{}/completions?api-version={}".format(api_base, deployment_id, api_version)
headers= { "api-key": api_key, "Content-Type": "application/json" }
body = {
    "prompt": '''
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. 

Human: Hello, who are you? 
AI: Hello, I am an AI assistant. I am here to help you with anything you need.
Human: I'd like to cancel my subscription. 
AI: 
    ''',
    "stream": stream,
    "temperature": 1,
    "max_tokens": 50,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    # "best_of": 1,
    "stop": "Human:"
}

response = requests.post(url, headers=headers, json=body)
status = response.status_code
if status == 400:
    print("Error: {}".format(response.json()['error']['message']))
    exit()

print(body["prompt"], end="", flush=True)

if stream:
    import json

    text = response.text.split('\n\n')
    for chunk in text:
        chunk = json.loads(chunk[6:])
        finish_reason = chunk["choices"][0]["finish_reason"]
        if finish_reason == None:
            time.sleep(0.05)
            print(chunk["choices"][0]["text"], end="", flush=True)
        else:
            break
else:
    response = response.json()
    content = response['choices'][0]['text']
    prompt_tokens = response['usage']['prompt_tokens']
    completion_tokens = response['usage']['completion_tokens']
    total_tokens = response['usage']['total_tokens']
    print(content)
    print("Prompt tokens: {}".format(prompt_tokens))
    print("Completion tokens: {}".format(completion_tokens))
    print("Total tokens: {}".format(total_tokens))