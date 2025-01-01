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
    prompt = f"User is asking for the simplest cli command to achieve the \
              following: '{user_request}'. Provide the best terminal command \
              without chaining or adding any additional operations. Respond \
              only in the following \
              JSON format: {{\"command\": \"your command here\"}}"

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
