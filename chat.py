import requests
import time
import importlib

# import variables "AZURE_OPENAI_API_KEY", "AZURE_OPENAI_API_ENDPOINT" from config.py
api_key = getattr(importlib.import_module("config_private"), "AZURE_OPENAI_API_KEY")
api_base = getattr(importlib.import_module("config_private"), "AZURE_OPENAI_API_ENDPOINT")
deployment_id = getattr(importlib.import_module("config_private"), "AZURE_OPENAI_API_DEPLOYMENT_ID")
stream = True

api_version = '2023-05-15'
url = "{}openai/deployments/{}/chat/completions?api-version={}".format(api_base, deployment_id, api_version)
headers= { "api-key": api_key, "Content-Type": "application/json" }
body = {
    "messages":[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure Cognitive Services support this too? Answer with no more than 15 words. "}
    ],
    "temperature": 1,
    "max_tokens": 800,
    "top_p": 0.95,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stream": stream,
    "stop": None
}
response = requests.post(url, headers=headers, json=body)
status = response.status_code

if status == 400:
    print("Error: {}".format(response.json()['error']['message']))
    exit()

for message in body["messages"]:
    print(message["role"] + ": " + message["content"])

if stream:
    import json

    text = response.text.split('\n\n')
    for chunk in text:
        chunk = json.loads(chunk[6:])
        finish_reason = chunk["choices"][0]["finish_reason"]
        if finish_reason == None:
            time.sleep(0.05)
            delta = chunk["choices"][0]["delta"]

            if "role" in delta.keys():
                print(delta["role"] + ": ", end="", flush=True)
            if "content" in delta.keys():
                print(delta["content"], end="", flush=True)
        else:
            break
else:
    response = response.json()
    content = response['choices'][0]['message']["content"]
    role = response['choices'][0]['message']["role"]
    prompt_tokens = response['usage']['prompt_tokens']
    completion_tokens = response['usage']['completion_tokens']
    total_tokens = response['usage']['total_tokens']
    print("{}: {}".format(role, content))
    print("Prompt tokens: {}".format(prompt_tokens))
    print("Completion tokens: {}".format(completion_tokens))
    print("Total tokens: {}".format(total_tokens))