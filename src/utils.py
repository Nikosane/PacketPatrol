import os

def ensure_directory_exists(directory):
    """
    Ensures that a directory exists, creating it if necessary.
    :param directory: Path to the directory
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

if __name__ == "__main__":
    directory = "../data/"
    ensure_directory_exists(directory)
