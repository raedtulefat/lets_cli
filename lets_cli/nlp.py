import requests
import json
import re
import os
from typing import Dict


# Function to read configuration
def read_config() -> Dict[str, str]:
    config_path = os.path.expanduser('~/.lets_cli_config')
    config = {}
    if os.path.exists(config_path):
        with open(config_path, 'r') as config_file:
            for line in config_file:
                key, value = line.strip().split('=')
                config[key] = value
    return config


def interpret_command(prompt: str) -> str:
    config = read_config()

    if config.get('api_choice') == 'ollama':
        url = f"{config.get('ollama_base_url')}/api/generate"

        payload = json.dumps({
            "model": "qwen2.5-coder:32b",
            "prompt": prompt,
            "stream": False
        })
        headers = {
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(url,
                                     headers=headers,
                                     data=payload,
                                     timeout=20)
            response.raise_for_status()
            response_data = response.json()

            response_text = response_data.get('response', '{}')

            match = re.search(r'\{\s*"command":\s*"(.*?)"\s*\}',
                              response_text,
                              re.DOTALL)
            if not match:
                match = re.search(
                    r'```.*?\{\s*"command":\s*"(.*?)"\s*\}.*?```',
                    response_text,
                    re.DOTALL)
            if not match:
                match = re.search(r'\{"command":\s*"(.*?)"\}', response_text)

            if match:
                interpreted_command = match.group(1)
            else:
                raise ValueError("Command not found in the response.")

        except (requests.RequestException, json.JSONDecodeError, ValueError) as e:
            if isinstance(e, requests.exceptions.Timeout):
                raise requests.exceptions.Timeout("The request timed out.")

            print(f"Error occurred: {str(e)}")

            if response:
                response_content = response.content.decode()
            else:
                response_content = 'No response'

            print(f"Response content: {response_content}")
            interpreted_command = (
                'echo "Error occurred. Please check the response content."'
            )

    elif config.get('api_choice') == 'openai':
        url = "https://api.openai.com/v1/chat/completions"

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.0
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {config.get('openai_key')}"
        }

        try:
            response = requests.post(url,
                                     headers=headers,
                                     json=payload,
                                     timeout=20)
            response.raise_for_status()
            response_data = response.json()

            response_text = response_data.get('choices', [{}])[0].get('message', {}).get('content', '{}')

            match = re.search(r'\{\s*"command":\s*"(.*?)"\s*\}',
                              response_text,
                              re.DOTALL)
            if not match:
                match = re.search(
                    r'```.*?\{\s*"command":\s*"(.*?)"\s*\}.*?```',
                    response_text,
                    re.DOTALL)
            if not match:
                match = re.search(r'\{"command":\s*"(.*?)"\}', response_text)

            if match:
                interpreted_command = match.group(1)
            else:
                raise ValueError("Command not found in the response.")

        except (requests.RequestException, json.JSONDecodeError, ValueError) as e:
            if isinstance(e, requests.exceptions.Timeout):
                raise requests.exceptions.Timeout("The request timed out.")

            print(f"Error occurred: {str(e)}")

            if response:
                response_content = response.content.decode()
            else:
                response_content = 'No response'

            print(f"Response content: {response_content}")
            interpreted_command = (
                'echo "Error occurred. Please check the response content."'
            )

    else:
        interpreted_command = 'echo "Error: API choice not supported."'

    return interpreted_command
