import os


def interactive_setup() -> None:
    print("Welcome to lets_cli setup!")
    choice = input("Choose between OpenAI or Ollama\
                   (type 'openai' or 'ollama'): ").strip().lower()

    config = {}
    if choice == 'openai':
        api_key = input("Enter your OpenAI API key: ").strip()
        config['api_choice'] = 'openai'
        config['openai_key'] = api_key
    elif choice == 'ollama':
        print("Enter your Ollama base URL")
        print("(e.g. http://10.0.0.55:11434)")
        base_url = input("ollama URL: ").strip()
        config['api_choice'] = 'ollama'
        config['ollama_base_url'] = base_url
    else:
        print("Invalid choice. Please run the setup again.")
        return

    # Save the configuration to a file in the user's home directory
    config_path = os.path.expanduser('~/.lets_cli_config')
    with open(config_path, 'w') as config_file:
        for key, value in config.items():
            config_file.write(f"{key}={value}\n")

    print("Configuration saved successfully.")
    print("\nTo check your configuration, run the following command:")
    print("On Linux or macOS:")
    print("  cat ~/.lets_cli_config")
    print("On Windows (PowerShell):")
    print("  Get-Content $env:USERPROFILE\\.lets_cli_config")


if __name__ == '__main__':
    interactive_setup()
