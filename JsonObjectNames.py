from enum import Enum


class GoalObject(Enum):
    Time = "Time"
    PartialResult = "PartialResult"
    TeamName = "TeamName"
    TeamUrl = "TeamUrl"
    Scorer = "Scorer"
    Assist = "Assist"
    IsPenaltyGoal = "IsPenaltyGoal"
    IsOwnGoal = "IsOwnGoal"
    IsHomeGoal = "IsHomeGoal"


class MatchInfoObject(Enum):
    MatchDate = "MatchDateFormatted"
    Results = "ResultsFormatted"
    Arena = "ActivityAreaName"
    HomeTeam = "HomeTeamName"
    AwayTeam = "AwayTeamName"


class PenaltyObject(Enum):
    HomeTeam = "HomeTeam"
    AwayTeam = "AwayTeam"
    Penalties = "Penalties"
    HomeTime = "HomeTime"
    HomePenalty = "HomePenalty"
    AwayTime = "AwayTime"
    AwayPenalty = "AwayPenalty"