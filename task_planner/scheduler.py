import random
from typing import cast

try:
    import pandas as pd
except ImportError as err:
    raise SystemExit("Installatie nodig: pip install pandas openpyxl") from err

from .config import AVOID_CONSECUTIVE
from .models import PlayerStats
from .utils import mkdate, parse_bool_ja_nee, to_int


def choose_candidates(
    players: list[str],
    week_index: int,
    already: set[str],
    stats: dict[str, PlayerStats],
    task_name: str,
    is_drive: bool,
) -> list[str]:
    def score(p: str) -> tuple[float, int, int, float]:
        ps = stats[p]
        return (
            ps.km if is_drive else 0.0,
            ps.per_task[task_name],
            ps.total_tasks,
            random.random(),
        )

    eligible = [p for p in players if p not in already]
    if AVOID_CONSECUTIVE:
        non_consec = [
            p
            for p in eligible
            if stats[p].last_week_index is None
            or cast(int, stats[p].last_week_index) < week_index - 0
        ]
        consec = [p for p in eligible if p not in non_consec]
        return sorted(non_consec, key=score) + sorted(consec, key=score)
    return sorted(eligible, key=score)


def assign_for_week(
    players: list[str],
    week_index: int,
    tasks_for_week: list[tuple[str, int]],
    stats: dict[str, PlayerStats],
    distance_km_single: float,
) -> dict[str, list[str]]:
    week_assignment: dict[str, list[str]] = {t: [] for t, _ in tasks_for_week}
    already: set[str] = set()

    for task_name, count in tasks_for_week:
        is_drive = task_name.casefold() == "rijden"
        for _ in range(count):
            candidates = choose_candidates(
                players, week_index, already, stats, task_name, is_drive
            )
            if not candidates:
                raise RuntimeError(
                    "Onvoldoende spelers om taken toe te wijzen."
                )

            chosen = next(
                (c for c in candidates if c not in week_assignment[task_name]),
                None,
            )
            if chosen is None:
                chosen = min(
                    players,
                    key=lambda p: (
                        stats[p].total_tasks,
                        stats[p].per_task[task_name],
                    ),
                )

            week_assignment[task_name].append(chosen)
            already.add(chosen)
            stats[chosen].per_task[task_name] += 1
            stats[chosen].total_tasks += 1
            stats[chosen].last_week_index = week_index
            if is_drive:
                stats[chosen].km += float(distance_km_single) * 2.0
    return week_assignment


def build_schedule(
    tasks_df: pd.DataFrame,
    matches_df: pd.DataFrame,
    players_df: pd.DataFrame,
    distances_df: pd.DataFrame,
):
    matches_df["date"] = [
        mkdate(y, m, d)
        for y, m, d in zip(
            matches_df["jaar"],
            matches_df["maand"],
            matches_df["dag"],
            strict=True,
        )
    ]
    matches_df["isUit"] = matches_df["isUit"].map(parse_bool_ja_nee)
    matches_df = matches_df.sort_values("date").reset_index(drop=True)

    players = players_df["displaynaam"].astype(str).tolist()
    if len(set(players)) != len(players):
        raise ValueError("Displaynamen moeten uniek zijn.")
    random.shuffle(players)

    dmap = {
        str(c).strip(): float(km)
        for c, km in zip(
            distances_df["club"], distances_df["afstand_km"], strict=True
        )
    }
    tasks = [
        (str(row["taak"]), str(row["scope"]), int(row["aantal"]))
        for _, row in tasks_df.iterrows()
    ]
    task_names = [t[0] for t in tasks]
    stats = {p: PlayerStats.empty(task_names) for p in players}

    out_rows: list[dict[str, str]] = []
    for idx, row in matches_df.iterrows():
        is_away = bool(row["isUit"])
        tegen = str(row["club"])
        datum = row["date"]

        tasks_for_week: list[tuple[str, int]] = []
        for name, scope, count in tasks:
            if (
                scope == "altijd"
                or (scope == "uit" and is_away)
                or (scope == "thuis" and not is_away)
            ):
                tasks_for_week.append((name, count))

        distance_single = dmap.get(tegen, 0.0)
        week_assignment = assign_for_week(
            players, to_int(idx), tasks_for_week, stats, distance_single
        )

        base: dict[str, str] = {
            "Datum": datum.strftime("%Y-%m-%d"),
            "Tegenstander": tegen,
            "Uit/Thuis": "Uit" if is_away else "Thuis",
        }
        for name, _, count in tasks:
            assigned = week_assignment.get(name, [])
            for i in range(count):
                base[f"{name} {i+1}"] = assigned[i] if i < len(assigned) else ""
        out_rows.append(base)

    schedule_df = pd.DataFrame(out_rows)

    stat_rows: list[dict[str, str | int | float]] = []
    for p, ps in stats.items():
        r: dict[str, str | int | float] = {
            "Speler": p,
            "Totaal taken": ps.total_tasks,
            "Km": round(ps.km, 1),
        }
        for t in task_names:
            r[f"{t} count"] = ps.per_task[t]
        stat_rows.append(r)
    stats_df = (
        pd.DataFrame(stat_rows)
        .sort_values(["Totaal taken", "Km", "Speler"])
        .reset_index(drop=True)
    )

    return schedule_df, stats_df
