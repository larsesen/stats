#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter


class Season(object):
    team_name = ""
    matches = []
    goals_for = []
    goals_against = []
    assists = []
    penalties = []
    top_scorers = []

    def __init__(self, team_name, matches):
        self.team_name = team_name
        self.matches = matches
        self.goals_for = get_goals_for(self, matches)
        self.goals_against = get_goals_against(self, matches)
        self.assists = get_assists_by_player(self.goals_for)
        self.penalties = get_penalties_by_player(get_penalties(self, matches))
        self.top_scorers = get_goals_grouped_by_player(self.goals_for)

    def __str__(self):
        return "Team name : {}" \
               "\nNumber of matches: {}" \
               "\nnumber of goals scored: {}" \
               "\nNumber of goals conceeded: {}" \
               "\nnumber of players with penalties: {}" \
               "\nnumber of goal scorers: {}" \
               "\n\nScorers: {}" \
               "\n\nAssists: {}" \
               "\n\nPenalties: {}" \
            .format(self.team_name, len(self.matches), len(self.goals_for), len(self.goals_against),
                    len(self.penalties), len(self.top_scorers),
                    print_entries_sorted(self.top_scorers),
                    print_entries_sorted(self.assists),
                    print_entries_sorted(self.penalties))


def get_penalties(self, matches):
    penalties = []

    for match in matches:
        for penalty in match.penalties:
            if penalty.team == self.team_name:
                penalties.append(penalty)
    return penalties


def get_goals_for(self, matches):
    goals = []
    for match in matches:
        for goal in match.goals:
            if goal.team == self.team_name:
                goals.append(goal)
    return goals


def get_goals_against(self, matches):
    goals = []
    for match in matches:
        for goal in match.goals:
            if goal.team != self.team_name:
                goals.append(goal)
    return goals


def get_assists(self, matches):
    assists = []
    for match in matches:
        for goal in match.goals:
            if goal.team == self.team_name and goal.assist != "":
                assists.append(goal.assist)
    return assists


def get_goals_grouped_by_player(goals):
    scorers = []
    for goal in goals:
        scorers.append(goal.scorer)
    return Counter(scorers)


def get_penalties_by_player(penalties):
    player_penalties = []
    for penalty in penalties:
        player_penalties.append(penalty.player)
    return Counter(player_penalties)


def get_assists_by_player(goals):
    assists = []
    for goal in goals:
        if goal.assist != "":
            assists.append(goal.assist)
    return Counter(assists)


def print_entries_sorted(top_scorers):
    s = ""
    for key, value in sorted(top_scorers.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        s += '\n' + key + ": " + str(value)
    return s.encode('utf-8')
