from task_planner.models import PlayerStats


def test_playerstats_empty_initializes_correctly():
    ps = PlayerStats.empty(["Rijden", "Fluiten"])
    assert ps.per_task == {"Rijden": 0, "Fluiten": 0}
    assert ps.total_tasks == 0
    assert ps.km == 0.0
    assert ps.last_week_index is None
