import os

def load_env(file_path=".env"):
    """
    Load environment variables from a .env file.
    :param file_path: Path to the .env file (default is ".env" in the current directory).
    """
    with open(file_path, "r") as f:
        for line in f:
            # Skip empty lines and lines starting with '#' (comments)
            if not line.strip() or line.startswith("#"):
                continue
            key, value = line.strip().split("=", 1)
            os.environ[key] = value

# Load environment variables from .env file when this module is imported
load_env()