import os
import signal
import time


# Signal handler function for the child process
def handle_signal(signum, frame):
    print(f"[Child] Received signal: {signum}. Proceeding...")


def main():

    # Create a pipe
    r, w = os.pipe()

    # Fork a child process
    pid = os.fork()

    if pid > 0:
        # Parent Process
        os.close(r)

        message = "Hello from parent via pipe!"
        os.write(w, message.encode())
        os.close(w)

        print(f"[Parent] Sent message to child: '{message}'")

        # Give child time to setup signal handler
        time.sleep(2)

        print("[Parent] Sending SIGUSR1 to child...")
        os.kill(pid, signal.SIGUSR1)

        # Wait for child to finish
        os.wait()

    else:
        # Child Process
        os.close(w)

        # Setup signal handler
        signal.signal(signal.SIGUSR1, handle_signal)

        # Read message from pipe
        message = os.read(r, 1024).decode()

        print(f"[Child] Received message: '{message}'")
        print("[Child] Waiting for SIGUSR1 signal from parent...")

        # Wait for signal
        signal.pause()

        print("[Child] Exiting.")


if __name__ == "__main__":
    main()