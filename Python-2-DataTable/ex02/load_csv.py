import pandas as pd


def valid_csv(path: str) -> bool:
    """Check if the given path is a valid CSV file."""
    if path is None:
        return False
    if not path.lower().endswith(".csv"):
        return False
    return True


def load(path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    try:
        if valid_csv(path) is False:
            return None
        df = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions", df.shape)
        return df
    except FileNotFoundError:
        print(f"No such file or directory: {path}")
        return None
