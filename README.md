# lets_cli

LANGUAGE EXECUTION TERMINAL SUPPORT (Lets)

## Description

`lets_cli` is a command-line tool that acts as an intelligent assistant for your CLI. It interprets natural language commands and translates them into executable shell commands, making it ideal for users who may not remember specific commands or want to streamline their workflow using plain English.

## Key Features

- **Natural Language Processing:** Converts plain English commands into shell commands using a powerful NLP model.
- **Interactive Execution:** Displays the interpreted command to the user and waits for confirmation before execution.
- **Ease of Use:** Simplifies terminal interactions, making it accessible even to those with limited command-line knowledge.

## Installation and setup

````bash
git clone https://github.com/raedtulefat/lets_cli.git
cd lets_cli
python3 -m venv venv
source venv/bin/activate
pip install .
lets_setup
```

# Example setup steps:
# Welcome to lets_cli setup!
# Choose between OpenAI or Ollama (type 'openai' or 'ollama'): ollama
# Enter your Ollama base URL
# (e.g. http://localhost:11434)
# ollama URL: http://localhost:11434
# Configuration saved successfully.

# Uninstall

```bash
sudo pip uninstall lets-cli
````

## Checking saved configuration

```bash
cat ~/.lets_cli_config
```

## Clearing previous build

```bash
rm -rf build dist *.egg-info
```

## Usage

```bash
lets show me a list of all docker containers currently running
```

## pid its running on

```
pgrep -af let
```

## Updating

```
pkill -f let
git pull origin master
lets
```

## How It Works

1. The user types a natural language command using the lets command.
2. lets_cli sends this input to an NLP API for interpretation.
3. The interpreted shell command is displayed to the user.
   Upon user confirmation, the command is executed in the terminal.

## Contribution

We welcome contributions from the community! Feel free to fork the repository, make improvements, and submit pull requests. Check out our Contributing Guidelines for more details.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Exmaple

User is asking for the simplest cli command to achieve the following: list all docker containers. Provide only a single command without chaining or adding any additional operations. Respond only in the following JSON format: {{\"command\": \"your command here\"}}"
