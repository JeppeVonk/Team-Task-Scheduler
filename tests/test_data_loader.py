from pathlib import Path

import pandas as pd
import pytest
from task_planner import data_loader


def test_load_csv_file_not_found(tmp_path: Path) -> None:
    fake_path = tmp_path / "doesnotexist.csv"
    with pytest.raises(SystemExit):
        data_loader.load_csv(str(fake_path))


def test_validate_columns_missing(tmp_path: Path) -> None:
    df = pd.DataFrame({"kolom1": [1, 2]})
    with pytest.raises(SystemExit):
        data_loader.validate_columns(df, {"kolom2"}, "test.csv")


def test_validate_columns_ok(tmp_path: Path) -> None:
    df = pd.DataFrame({"kolom1": [1], "kolom2": [2]})
    # Geen error verwacht
    data_loader.validate_columns(df, {"kolom1", "kolom2"}, "test.csv")
