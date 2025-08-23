import argparse
import random

from . import data_loader, exporter, scheduler
from .config import HOME_TEAM_NAME, RANDOM_SEED


def run_with_args(args: argparse.Namespace) -> str:
    random.seed(args.seed)

    df_t = data_loader.load_csv(args.taken)
    df_w = data_loader.load_csv(args.wedstrijden)
    df_s = data_loader.load_csv(args.spelers)
    df_a = data_loader.load_csv(args.afstanden)

    data_loader.validate_columns(df_t, {"taak", "scope", "aantal"}, args.taken)
    data_loader.validate_columns(
        df_w,
        {"jaar", "maand", "dag", "club", "team", "isUit"},
        args.wedstrijden,
    )
    data_loader.validate_columns(df_s, {"naam", "displaynaam"}, args.spelers)
    data_loader.validate_columns(df_a, {"club", "afstand_km"}, args.afstanden)

    schedule_df, stats_df = scheduler.build_schedule(df_t, df_w, df_s, df_a)

    exporter.export_excel(
        schedule_df,
        stats_df,
        players=list(df_s["displaynaam"].astype(str)),
        out_path=args.uitvoer,
    )

    return str(args.uitvoer)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=f"{HOME_TEAM_NAME} taakplanner"
    )
    parser.add_argument("--taken", required=True)
    parser.add_argument("--wedstrijden", required=True)
    parser.add_argument("--spelers", required=True)
    parser.add_argument("--afstanden", required=True)
    parser.add_argument("--uitvoer", default="schema.xlsx")
    parser.add_argument("--seed", type=int, default=RANDOM_SEED)
    args = parser.parse_args()

    uitvoer = run_with_args(args)

    print(f"Gereed: {uitvoer}")


if __name__ == "__main__":
    main()
