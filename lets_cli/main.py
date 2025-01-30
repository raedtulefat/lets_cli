import subprocess
import sys
from lets_cli.nlp import interpret_command
from lets_cli.spinner import Spinner
import requests


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: lets <natural language command>")
        sys.exit(1)

    # Join the command-line arguments into a single prompt
    user_request = ' '.join(sys.argv[1:])
    prompt = f"""
                YOU ARE `@LETS_AGENT`, AN EXPERT LINUX COMMAND GENERATOR. YOUR SOLE PURPOSE IS TO PROVIDE PRECISE, EFFICIENT, AND SECURE LINUX COMMANDS BASED ON USER REQUESTS.

                ###INSTRUCTIONS###

                - READ AND UNDERSTAND THE USER REQUEST: '{user_request}'
                - IDENTIFY THE MOST APPROPRIATE LINUX COMMAND TO ACHIEVE THE DESIRED TASK
                - ENSURE THE COMMAND IS EFFICIENT, SECURE, AND FOLLOWS BEST PRACTICES
                - AVOID COMMANDS THAT COULD BE POTENTIALLY DESTRUCTIVE UNLESS CLEARLY REQUESTED
                - DO NOT PROVIDE EXPLANATIONS OR ADDITIONAL CONTEXT—ONLY RETURN THE COMMAND

                ###WHAT NOT TO DO###

                - **NEVER** RESPOND WITH ANYTHING OTHER THAN THE REQUIRED COMMAND
                - **NEVER** INCLUDE UNSAFE COMMANDS (E.G., `rm -rf /` UNLESS SPECIFICALLY REQUESTED)
                - **NEVER** ASK FOR CLARIFICATION—ALWAYS PROVIDE THE BEST COMMAND BASED ON THE GIVEN REQUEST
                - **NEVER** INCLUDE PLACEHOLDERS—ALWAYS USE LITERAL COMMAND SYNTAX

                ###RESPONSE FORMAT###

                Respond only in the following JSON format:
                {{"command": "your command here"}}
                """

    spinner = Spinner(message="Thinking", delay=0.08)

    try:
        # Initialize and start the spinner
        spinner.start()

        # Get the interpreted command from the API
        interpreted_command = interpret_command(prompt)

        # Stop the spinner
        spinner.stop()

        if "Error occurred" in interpreted_command:
            print(interpreted_command)
        else:
            print(f'Interpreted Command: {interpreted_command}')
            print('Press Enter to execute...')
            input()  # Wait for user confirmation

            # Execute the command using subprocess
            process = subprocess.Popen(interpreted_command,
                                       shell=True,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                print(stdout.decode())
            else:
                print("Error:\n", stderr.decode())

    except (KeyboardInterrupt, requests.exceptions.Timeout):
        spinner.stop()
        print("\nExecution interrupted due to timeout. Exiting...")

    except Exception as e:
        spinner.stop()
        print(f"\nAn error occurred: {str(e)}")

    finally:
        spinner.stop()


if __name__ == '__main__':
    main()
