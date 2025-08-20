from datetime import date

import pytest
from task_planner.utils import (
    hashed_color_hex,
    mkdate,
    parse_bool_ja_nee,
    shuffle_players,
    to_int,
)


def test_parse_bool_ja_nee_true_cases():
    for v in ["ja", "JA", "y", "Yes", "1", "true"]:
        assert parse_bool_ja_nee(v)


def test_parse_bool_ja_nee_false_cases():
    for v in ["nee", "n", "0", "false", "onzin"]:
        assert not parse_bool_ja_nee(v)


def test_mkdate_returns_date():
    d = mkdate("2025", "9", "7")
    assert isinstance(d, date)
    assert d == date(2025, 9, 7)


def test_to_int_from_int_and_str():
    assert to_int(5) == 5
    assert to_int("42") == 42
    with pytest.raises(TypeError):
        to_int(3.14)


def test_hashed_color_hex_format():
    color = hashed_color_hex("Jan")
    assert isinstance(color, str)
    assert len(color) == 6
    int(color, 16)  # moet parsebaar zijn als hex


def test_shuffle_players_deterministic():
    players = ["A", "B", "C", "D"]
    shuffled1 = shuffle_players(players.copy(), seed=123)
    shuffled2 = shuffle_players(players.copy(), seed=123)
    assert shuffled1 == shuffled2
