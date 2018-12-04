from ReadFile import read_json_data
import dto.Goal as Goal

from os import listdir
from os.path import isfile, join


from GoalConstants import GoalAccessObjects as gao


def get_matches_from_directory(directory):
    only_files = [f for f in listdir(directory) if isfile(join(directory, f))]
    return only_files


def get_goals_from_file(path):
    all_data = read_json_data(path)
    goals = []
    for goal in all_data:

        scorer = goal[gao.Scorer]
        assist = goal[gao.Assist]
        partial_result = goal[gao.PartialResult]
        team_name = goal[gao.TeamName]
        time = goal[gao.Time]

        if time != 'Str': #penalty shootout does not have time
            current = Goal.Goal(scorer, assist, partial_result, team_name, time)
            goals.append(current)

    return goals
