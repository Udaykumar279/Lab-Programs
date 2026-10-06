import os
import subprocess
import shlex


def run_shell():
    while True:
        try:
            # Display prompt and get input
            command = input("mysh> ").strip()

            if not command:
                continue

            # Exit command
            if command.lower() == 'exit':
                print("Exiting shell...")
                break

            # Handle 'cd' command separately
            if command.startswith("cd "):
                path = command[3:].strip()

                try:
                    os.chdir(path)
                except FileNotFoundError:
                    print(f"No such directory: {path}")

                continue

            # Parse command using shlex
            args = shlex.split(command)

            # Execute external command
            result = subprocess.run(
                args,
                capture_output=True,
                text=True
            )

            print(result.stdout, end='')

            if result.stderr:
                print(result.stderr, end='')

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")

        except Exception as e:
            print(f"Error: {e}")


# Run the shell
if __name__ == "__main__":
    run_shell()