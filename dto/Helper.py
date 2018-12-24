from enum import Enum


class MatchResult(Enum):
    WIN = 'Victory',
    WIN_PEN = 'Victory pen',
    LOSS_PEN = 'Loss pen'
    LOSS = 'Loss'
