import configparser
from openai import OpenAI

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        return config['Settings']['Model'],config['Settings']['ModelApiKey']
    except KeyError:
        raise KeyError("Cannot find 'ModelApiKey' in 'Settings' section of config.ini")

def create_openai_client():
    model,api_key = get_api_key()
    try:
        client = OpenAI(
            api_key=api_key,
            timeout=60,
        )
        return model,client
    except Exception as e:
        print(f"[OpenAI] Failed to create client: {str(e)}")
        raise
