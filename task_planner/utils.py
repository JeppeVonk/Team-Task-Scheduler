import hashlib
import random
from collections.abc import Hashable
from datetime import date

from .config import RANDOM_SEED


def parse_bool_ja_nee(v: str) -> bool:
    return str(v).strip().casefold() in {"ja", "j", "y", "yes", "true", "1"}


def mkdate(y: str, m: str, d: str) -> date:
    return date(int(y), int(m), int(d))


def hashed_color_hex(name: str) -> str:
    h = hashlib.sha1(name.encode("utf-8")).hexdigest()
    r = (int(h[0:2], 16) + 255) // 2
    g = (int(h[2:4], 16) + 255) // 2
    b = (int(h[4:6], 16) + 255) // 2
    return f"{r:02X}{g:02X}{b:02X}"


def shuffle_players(players: list[str], seed: int = RANDOM_SEED) -> list[str]:
    rnd = random.Random(seed)
    rnd.shuffle(players)
    return players


def to_int(x: Hashable) -> int:
    if isinstance(x, int):
        return x
    elif isinstance(x, str):
        return int(x)
    else:
        raise TypeError(f"Kan {type(x)} niet converteren naar int")
