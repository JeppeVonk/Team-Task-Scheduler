import sys

try:
    import pandas as pd
except ImportError as err:
    raise SystemExit("Installatie nodig: pip install pandas openpyxl") from err


def load_csv(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)  # pyright: ignore[reportUnknownMemberType]
    except FileNotFoundError:
        sys.exit(f"Bestand niet gevonden: {path}")


def validate_columns(df: pd.DataFrame, required: set[str], name: str) -> None:
    if not required.issubset(df.columns):
        missing = sorted(required - set(df.columns))
        sys.exit(f"{name} mist kolommen: {missing}")
