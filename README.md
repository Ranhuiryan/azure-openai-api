# Azure OpenAI API examples

Some examples based on Azure OpenAI API.

## Prerequisites

- An Azure subscription
- Access granted to Azure OpenAI Service in the desired Azure subscription. Currently, access to this service is granted only by application. You can apply for access to Azure OpenAI Service by completing the form at [https://aka.ms/oai/access](https://aka.ms/oai/access).
- Python 3.7.1 or later version.
- The following Python libraries: os.
- An Azure OpenAI Service resource with either the `gpt-35-turbo` or the `text-*` models deployed. 

## Installation

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Configuration

To use the Azure OpenAI API, you will need to provide an API key and endpoint. These should be stored in a `config_private.py` file in the root directory of the project. The file should define the following variables:

```python
AZURE_OPENAI_API_KEY = "your-api-key"
AZURE_OPENAI_API_ENDPOINT = "https://your-api-endpoint.com/"
AZURE_OPENAI_API_DEPLOYMENT_ID = "your-deployment-id"
```

## DALL-E Image Generation

Generates images using the DALL-E API from Azure OpenAI. It takes a prompt as input and generates one or more images based on the prompt.

### Usage

To generate images, run the `dalle.py` script. This will generate one or more images based on the prompt. The images will be printed to the console as URLs.

## Azure OpenAI Chatbot

This project demonstrates how to use the Azure OpenAI API to create a chatbot. It uses the requests library to send requests to the API and receive responses.

### Usage

To use the chatbot, run the `chat.py` script. This will send a series of messages to the API and print the responses to the console.

## Azure OpenAI Completion Chatbot

This project demonstrates how to use the Azure OpenAI API to create a completion chatbot. It uses the requests library to send requests to the API and receive responses.

### Usage

To use the chatbot, run the `completion.py` script. This will send a series of messages to the API and print the responses to the console.