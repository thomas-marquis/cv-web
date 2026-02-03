import datetime as dt
from dataclasses import dataclass


@dataclass(frozen=True)
class TimePeriod:
    start: dt.datetime | None
    end: dt.datetime | None
