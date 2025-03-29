import os

def list_directory_contents(directory_path):
    try:
        # Retrieve the list of all entries in the specified directory
        entries = os.listdir(directory_path)
        print(f"Contents of '{directory_path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing '{directory_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
directory = '/'  # Replace with your target directory path
list_directory_contents(directory)
