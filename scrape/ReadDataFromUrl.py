#!/usr/bin/env python
# -*- coding: utf-8 -*-

#### Deprecated

import objects.Match as Match
from ReadFile import read_json_data
import objects.MatchEvent as MatchEvent
import objects.MatchInfo as Info

from JsonObjectNames import GoalObject as GoalObject
from JsonObjectNames import MatchInfoObject as MatchObject
from JsonObjectNames import PenaltyObject as PenaltyObject


import urllib

base_url = "https://wp.nif.no/PageMatchWithResult.aspx?LinkId="
match_id = "6861087"

f = urllib.urlopen(base_url + match_id)
my_file = f.read()

last_part = my_file.split('var teamVM =')[1]
team_vm = my_file.split('var teamVM =')[1].split(',\"BindingContainerId\"')[0]



def get_variable_from_file(variable_name):
    return last_part.split(variable_name)[1].split("\n")[0]


def get_contents_with_brackets(headline, variable):
    string = "\"{}\": [".format(headline)
    string += variable[:-3]
    string += "}],"
    return string



match_info = get_variable_from_file('var matchBasicInfoVM =')
match_statistics = get_variable_from_file('var matchStatistics =')
goals_in_order = get_variable_from_file('var goalsInOrderVM =')
match_penalties = get_variable_from_file('var matchPenaltiesVM =')

all_info = "{"

all_info += "\"{}\": [".format('teams')
all_info += team_vm
all_info += '}],'

#all_info += get_contents_with_brackets("teams", team_vm)
all_info += get_contents_with_brackets("match_info", match_info)
all_info += get_contents_with_brackets("match_statistics", match_statistics)

all_info += get_contents_with_brackets("goals_in_order", goals_in_order)
all_info += get_contents_with_brackets("match_penalties", match_penalties)

all_info = all_info[:-1] # removing last comma
all_info += "}"

with open('test.json', 'w') as file:
    file.write(all_info)

#print all_info


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
    for entry in all_data['goals_in_order']:
        for goal in entry['goalsInOrder']:

            scorer = goal[GoalObject.Scorer]
            assist = goal[GoalObject.Assist]
            partial_result = goal[GoalObject.PartialResult]
            team_name = goal[GoalObject.TeamName]
            time = goal[GoalObject.Time]

            if time == 'Str':
                scorer = "Penalty shootout"
                time = "3 - 20:00"

            current = MatchEvent.Goal(scorer, assist, partial_result, team_name, time)
            goals.append(current)
    return goals


def extract_penalties(all_data):
    all_penalties = []

    for penalty in all_data['match_penalties']:

        home_team = penalty[PenaltyObject.HomeTeam]
        away_team = penalty[PenaltyObject.AwayTeam]
        match_penalties = penalty[PenaltyObject.Penalties]

        for match_penalty in match_penalties:
            home_time = match_penalty[PenaltyObject.HomeTime]
            home_penalty = match_penalty[PenaltyObject.HomePenalty]
            away_time = match_penalty[PenaltyObject.AwayTime]
            away_penalty = match_penalty[PenaltyObject.AwayPenalty]

            if home_time != "":
                current = MatchEvent.Penalty(home_team, home_time, home_penalty)
                all_penalties.append(current)

            if away_time != "":
                current = MatchEvent.Penalty(away_team, away_time, away_penalty)
                all_penalties.append(current)

    return all_penalties


match_info, goals, penalties = get_data_from_file('test.json')
match = Match.Match(match_info, goals, penalties)
print match
