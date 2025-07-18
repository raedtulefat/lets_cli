# lets_cli

LANGUAGE EXECUTION TERMINAL SUPPORT (Lets)

## Description

`lets_cli` is a command-line tool that acts as an intelligent assistant for your CLI. It interprets natural language commands and translates them into executable shell commands, making it ideal for users who may not remember specific commands or want to streamline their workflow using plain English.

## Key Features

- **Natural Language Processing:** Converts plain English commands into shell commands using a powerful NLP model.
- **Interactive Execution:** Displays the interpreted command to the user and waits for confirmation before execution.
- **Ease of Use:** Simplifies terminal interactions, making it accessible even to those with limited command-line knowledge.

# Clone the repository

```bash
git clone https://github.com/raedtulefat/lets_cli.git
cd lets_cli
```

# Create a virtual environment and activate it

```bash
python3 -m venv venv
source venv/bin/activate
```

# Install the package and configure

## For Development

```bash
Developer Mode (Editable Install with Virtual Environment)

# Clone the repo
git clone https://github.com/raedtulefat/lets_cli.git
cd lets_cli

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install in editable (dev) mode
pip install -e .

# Run setup
lets_setup
```

## For real use (GLobal Install)

```bash
Global User Install (For Regular Use)
# First make sure you're *not* in a virtual environment:
deactivate  # if active

# Navigate to the project folder
cd lets_cli

# Install globally for your user
pip install --user .

# For most systems, add this to ~/.zshrc or ~/.bash_profile:
export PATH="$HOME/Library/Python/3.9/bin:$HOME/.local/bin:$PATH"

# Reload your shell
source ~/.zshrc  # or ~/.bash_profile
```

# Updating Your Global Install

```bash
lets --version

# Go to your lets_cli project folder
cd lets_cli

# Pull latest changes
git pull origin master

# Reinstall globally (not needed if using editable dev mode)
pip install --user .
```

Welcome to lets_cli setup!

> Choose between OpenAI or Ollama (type 'openai' or 'ollama'): ollama
> Enter your Ollama base URL
> (e.g. http://localhost:11434)
> ollama URL: http://localhost:11434
> Configuration saved successfully.

````

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
source venv/bin/activate
lets show me a list of all docker containers currently running
```

## Checking your version

```bash
lets --version
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

## Recommended OpenAI Models

gpt-3.5-turbo offers a good balance of cost and reasoning. For heavier reasoning tasks you can switch to gpt-4-turbo.

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

lets_cli | master > lets list all md files  
Interpreted Command: find . -type f -name '\*.md'
Press ⏎ to execute...

./CODE_OF_CONDUCT.md
./LICENSE.md
./CHANGELOG.md
./README.md
./CONTRIBUTING.md
