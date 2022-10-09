from enum import Enum


class ResultType(Enum):
    ignore = 1
    service_or_ident = 2
    ident = 3
    const = 4
