from dataclasses import dataclass


@dataclass
class PlayerStats:
    per_task: dict[str, int]
    total_tasks: int
    km: float
    last_week_index: int | None

    @staticmethod
    def empty(task_names: list[str]) -> "PlayerStats":
        return PlayerStats(
            per_task={t: 0 for t in task_names},
            total_tasks=0,
            km=0.0,
            last_week_index=None,
        )
