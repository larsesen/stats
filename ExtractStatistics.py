#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MapFileToObjects
from dto import Match, Season


def get_all_matches(directory, file_names):
    matches = []
    for file_name in sorted(file_names):
        match_info, goals, penalties = MapFileToObjects.get_data_from_file(directory + file_name)
        match = Match.Match(match_info, goals, penalties)
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
