import pandas as pd
import pytest
from task_planner import models, scheduler


def test_choose_candidates_filters_and_orders():
    players = ["Jan", "Piet"]
    stats = {p: models.PlayerStats.empty(["Rijden"]) for p in players}
    preferences = {
        "Jan": {"Rijden": 2},
        "Piet": {"Rijden": 0},
    }  # Piet kan niet rijden
    result = scheduler.choose_candidates(
        players, 0, set(), stats, "Rijden", True, preferences
    )
    assert result == ["Jan"]


def test_assign_for_week_raises_when_no_candidates():
    players = ["Jan"]
    stats = {p: models.PlayerStats.empty(["Fluiten"]) for p in players}
    preferences = {"Jan": {"Fluiten": 0}}
    with pytest.raises(RuntimeError):
        scheduler.assign_for_week(
            players, 0, [("Fluiten", 1)], stats, 0.0, preferences
        )


def test_build_schedule_minimal():
    tasks_df = pd.DataFrame(
        [
            {"taak": "Rijden", "scope": "uit", "aantal": 1},
            {"taak": "Fluiten", "scope": "thuis", "aantal": 1},
        ]
    )
    matches_df = pd.DataFrame(
        [
            {
                "jaar": 2025,
                "maand": 9,
                "dag": 7,
                "club": "Testclub",
                "team": "H1",
                "isUit": "ja",
            },
            {
                "jaar": 2025,
                "maand": 9,
                "dag": 14,
                "club": "Testclub",
                "team": "H1",
                "isUit": "nee",
            },
        ]
    )
    players_df = pd.DataFrame(
        [
            {"naam": "Jan", "displaynaam": "Jan", "Rijden": 2, "Fluiten": 2},
            {"naam": "Piet", "displaynaam": "Piet", "Rijden": 2, "Fluiten": 2},
        ]
    )
    distances_df = pd.DataFrame([{"club": "Testclub", "afstand_km": 10}])

    schedule_df, stats_df = scheduler.build_schedule(
        tasks_df, matches_df, players_df, distances_df
    )

    # Schema moet 2 rijen bevatten (voor 2 wedstrijden)
    assert len(schedule_df) == 2
    # Stats moet 2 spelers bevatten
    assert set(stats_df["Speler"]) == {"Jan", "Piet"}
    # Km moeten afgerond zijn
    assert all(isinstance(x, float) for x in stats_df["Km"])
