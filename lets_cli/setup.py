import os
import json
import re
import requests

def save_config(config: dict, config_path: str) -> None:
    """Saves the configuration to the specified file."""
    with open(config_path, 'w') as config_file:
        for key, value in config.items():
            config_file.write(f"{key}={value}\n")

def get_config_path() -> str:
    """Returns the path to the configuration file."""
    return os.path.expanduser('~/.lets_cli_config')

def read_config() -> dict:
    """Reads the configuration from the specified file."""
    config_path = get_config_path()
    config = {}
    if os.path.exists(config_path):
        with open(config_path, 'r') as config_file:
            for line in config_file:
                key, value = line.strip().split('=', 1)
                config[key] = value
    else:
        print("Configuration file not found. Please run the setup again.")
    return config

def interpret_command(prompt: str) -> str:
    config = read_config()

    if config.get('api_choice') == 'ollama':
        url = f"{config.get('ollama_base_url')}/api/generate"

        payload = json.dumps({
            "model": "qwen2.5-coder:latest",
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
            "model": "gpt-3.5-turbo",
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

def interactive_setup() -> None:
    """Interactive setup for lets_cli to configure API settings."""
    print("Welcome to lets_cli setup!")
    choice = input("Choose between OpenAI or Ollama (type 'openai' or 'ollama'): ").strip().lower()

    config = {}
    if choice == 'openai':
        api_key = input("Enter your OpenAI API key: ").strip()
        config['api_choice'] = 'openai'
        config['openai_key'] = api_key
    elif choice == 'ollama':
        print("Enter your Ollama base URL")
        print("(e.g. http://localhost:11434)")
        base_url = input("Ollama URL: ").strip()
        config['api_choice'] = 'ollama'
        config['ollama_base_url'] = base_url
    else:
        print("Invalid choice. Please run the setup again.")
        return

    # Save the configuration to the file
    config_path = get_config_path()
    save_config(config, config_path)

    print("Configuration saved successfully.")
    print("\nTo check your configuration, run the following command:")
    print("On Linux or macOS:")
    print("  cat ~/.lets_cli_config")
    print("On Windows (PowerShell):")
    print("  Get-Content $env:USERPROFILE\\.lets_cli_config")

if __name__ == '__main__':
    interactive_setup()
