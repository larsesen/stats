from enum import Enum


class AccessObjects(Enum):
    Time = "Time"
    PartialResult = "PartialResult"
    TeamName = "TeamName"
    TeamUrl = "TeamUrl"
    Scorer = "Scorer"
    Assist = "Assist"
    IsPenaltyGoal = "IsPenaltyGoal"
    IsOwnGoal = "IsOwnGoal"
    IsHomeGoal = "IsHomeGoal"
