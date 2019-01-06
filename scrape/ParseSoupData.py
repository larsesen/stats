#!/usr/bin/env python
# -*- coding: utf-8 -*-

# todo Make this class read from all files in match_reports
import MapFileToObjects
from ReadFile import read_json_data


import dto.Match as Match
import dto.MatchEvent as MatchEvent
import dto.MatchInfo as Info

from JsonObjectNames import GoalObject as GoalObject
from JsonObjectNames import MatchInfoObject as MatchObject
from JsonObjectNames import PenaltyObject as PenaltyObject
from dto import Season


def extract_match_info(all_data):
    info = all_data['info'][0]
    match_date = info[MatchObject.MatchDate]
    arena = info[MatchObject.Arena]
    home_team = info[MatchObject.HomeTeam]
    away_team = info[MatchObject.AwayTeam]
    end_result = info[MatchObject.Results]
    match_info = Info.MatchInfo(match_date, arena, home_team, away_team, end_result)
    return match_info


def extract_goals(all_data):
    goals = []
    for entry in all_data['goals']:
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

    for penalty in all_data['pens']:

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


def get_data_from_file(path):
    all_data = read_json_data(path)
    match_info = extract_match_info(all_data)
    goals = extract_goals(all_data)
    penalties = extract_penalties(all_data)
    return match_info, goals, penalties


directory = "match_reports/"
file_names = MapFileToObjects.get_files_from_directory(directory)

matches = []
for file_name in sorted(file_names):
    match_info, goals, penalties = MapFileToObjects.get_data_from_file(directory + file_name)
    match = Match.Match(match_info, goals, penalties)
    matches.append(match)


team_names = ['Lyn','BMIL','Ull/Kisa','Grei','Lillestrøm','Ajer','Øreåsen','Vålerenga']
season_stats_for_team = []
for team_name in team_names:
    season = Season.Season(team_name, matches)
    season_stats_for_team.append(season)

print 'Team \t\t  K  S  US UT T  Goals  +-  P \n'
for season in sorted(season_stats_for_team, key=lambda x: x.points, reverse=True):
    print season


