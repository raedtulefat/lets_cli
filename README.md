# lets_cli

## Description

`lets_cli` is a command-line tool that acts as an intelligent assistant for your terminal. It allows users to input natural language commands, which are then interpreted and translated into executable shell commands. This tool is particularly useful for those who may not remember exact terminal commands or want to streamline their workflow by using plain English.

## Key Features

- **Natural Language Processing:** Converts plain English commands into shell commands using a powerful NLP model.
- **Interactive Execution:** Displays the interpreted command to the user and waits for confirmation before execution.
- **Ease of Use:** Simplifies terminal interactions, making it accessible even to those with limited command-line knowledge.

## Installation and setup

```bash
git clone https://github.com/raedtulefat/lets_cli.git
cd lets_cli
pip install -r requirements.txt
lets_setup
```

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

## How It Works

1. The user types a natural language command using the lets command.
2. lets_cli sends this input to an NLP API for interpretation.
3. The interpreted shell command is displayed to the user.
   Upon user confirmation, the command is executed in the terminal.

## Contribution

We welcome contributions from the community! Feel free to fork the repository, make improvements, and submit pull requests. Check out our Contributing Guidelines for more details.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
