from ReadFile import read_json_data
import dto.Goal as Goal
import dto.MatchInfo as Info
import dto.Penalty as Penalty

from os import listdir
from os.path import isfile, join


from JsonObjectNames import GoalObject as GoalObject
from JsonObjectNames import MatchInfoObject as MatchObject
from JsonObjectNames import PenaltyObject as PenaltyObject


def get_files_from_directory(directory):
    only_files = [f for f in listdir(directory) if isfile(join(directory, f))]
    return only_files


def get_data_from_file(path):
    all_data = read_json_data(path)
    match_info = extract_match_info(all_data)
    goals = extract_goals(all_data)
    penalties = extract_penalties(all_data)
    return match_info, goals, penalties


def extract_match_info(all_data):
    info = all_data['match_info'][0]
    match_date = info[MatchObject.MatchDate]
    arena = info[MatchObject.Arena]
    home_team = info[MatchObject.HomeTeam]
    away_team = info[MatchObject.AwayTeam]
    end_result = info[MatchObject.Results]
    match_info = Info.MatchInfo(match_date, arena, home_team, away_team, end_result)
    return match_info


def extract_goals(all_data):
    goals = []
    for goal in all_data['goals']:

        scorer = goal[GoalObject.Scorer]
        assist = goal[GoalObject.Assist]
        partial_result = goal[GoalObject.PartialResult]
        team_name = goal[GoalObject.TeamName]
        time = goal[GoalObject.Time]

        if time == 'Str':
            scorer = "Penalty shootout"
            time = "3 - 20:00"

        current = Goal.Goal(scorer, assist, partial_result, team_name, time)
        goals.append(current)
    return goals


def extract_penalties(all_data):
    all_penalties = []

    for penalty in all_data['penalties']:

        home_team = penalty[PenaltyObject.HomeTeam]
        away_team = penalty[PenaltyObject.AwayTeam]
        match_penalties = penalty[PenaltyObject.Penalties]

        for match_penalty in match_penalties:
            home_time = match_penalty[PenaltyObject.HomeTime]
            home_penalty = match_penalty[PenaltyObject.HomePenalty]
            away_time = match_penalty[PenaltyObject.AwayTime]
            away_penalty = match_penalty[PenaltyObject.AwayPenalty]

            if home_time != "":
                current = Penalty.Penalty(home_team, home_time, home_penalty)
                all_penalties.append(current)

            if away_time != "":
                current = Penalty.Penalty(away_team, away_time, away_penalty)
                all_penalties.append(current)

    return all_penalties