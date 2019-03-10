#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MapFileToObjects
from objects import Match, Season
from objects.Constants import MatchResult


def get_all_matches(directory, file_names):
    matches = []
    for file_name in sorted(file_names):
        match_info, goals, penalties, home_players, away_players = MapFileToObjects.get_data_from_file(directory + file_name)
        match = Match.Match(match_info, goals, penalties, home_players, away_players)
        matches.append(match)
    return matches


def get_all_season_data(matches):
    data_for_season = []
    team_names = ['Lyn', 'BMIL', 'Ull/Kisa', 'Grei', 'Lillestrøm', 'Ajer', 'Øreåsen', 'Vålerenga']
    for team_name in team_names:
        data_for_season.append(Season.Season(team_name, matches))
    return data_for_season


def get_timestamp_for_goals(data_for_season):
    all_goals = []
    for entry in data_for_season:
        for goal in entry.goals_for:
            all_goals.append(goal.sort_stamp)
    return sorted(all_goals)


def get_timestamp_for_penalties(data_for_season):
    all_penalties = []
    for entry in data_for_season:
        for penalty in entry.penalties:
            all_penalties.append(penalty.sort_stamp)
    return sorted(all_penalties)


def get_timestamps_within_period(timestamps):
    timestamps_within_period = []
    for timestamp in timestamps:
        timestamp = timestamp % 1200
        if timestamp == 0:
            timestamp = 1200
        timestamps_within_period.append(timestamp)
    return timestamps_within_period


def get_matches_for_team(matches, team_name):
    matches_for_team = []
    for match in matches:
        if unicode(match.home_team).encode('utf-8') == team_name or unicode(match.away_team).encode('utf-8') == team_name:
            matches_for_team.append(match)
    return matches_for_team


def get_points_per_game_for_player(matches_for_team, name):
    point_list = [0] # removes off-by-one error in graph
    for m in matches_for_team:
        point = 0
        if m.home_team == 'BMIL':
            for player in m.home_players:
                if player.name == name:
                    point = player.points
            point_list.append(point)
        elif m.away_team == 'BMIL':
            for player in m.away_players:
                if player.name == name:
                    point = player.points
                    break
            point_list.append(point)
    return point_list


def get_match_results_as_points(matches_for_team, team_name):
    results = get_match_results(matches_for_team, team_name)
    points = [0] # removes off-by-one error in graph
    for result in results:
        if result == MatchResult.WIN:
            points.append(3)
        elif result == MatchResult.WIN_PEN:
            points.append(2)
        elif result == MatchResult.LOSS_PEN:
            points.append(1)
        elif result == MatchResult.LOSS:
            points.append(0)
        else:
            raise ValueError('Could not find points for match result')
    return points


def get_match_results(matches_for_team, team_name):
    match_results = []
    for match in matches_for_team:
        if unicode(match.home_team).encode('utf-8') == team_name:
            match_results.append(match.match_info.result_for_home_team)
        elif unicode(match.away_team).encode('utf-8') == team_name:
            match_results.append(match.match_info.result_for_away_team)
    return match_results
