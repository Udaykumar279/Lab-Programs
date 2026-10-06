import os

def create_file(filename):
    with open(filename, 'w') as f:
        f.write("This is a test file created by Python shell script.\n")
    print(f"File '{filename}' created.")


def read_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            print(f"\nContents of '{filename}':")
            print(f.read())
    else:
        print(f"File '{filename}' not found.")


def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted.")
    else:
        print(f"File '{filename}' does not exist.")


# Main logic
filename = "my_file.txt"

create_file(filename)
read_file(filename)
delete_file(filename)