from ReadFile import read_json_data
import dto.Goal as Goal
import dto.MatchInfo as Info

from os import listdir
from os.path import isfile, join


from JsonObjectNames import GoalObject as GoalObject
from JsonObjectNames import MatchInfoObject as MatchObject


def get_matches_from_directory(directory):
    only_files = [f for f in listdir(directory) if isfile(join(directory, f))]
    return only_files


def get_goals_from_file(path):
    all_data = read_json_data(path)
    goals = extract_goals(all_data)
    match_info = extract_match_info(all_data)

    return goals, match_info


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

        if time != 'Str':  # penalty shootout does not have time
            current = Goal.Goal(scorer, assist, partial_result, team_name, time)
            goals.append(current)
    return goals
