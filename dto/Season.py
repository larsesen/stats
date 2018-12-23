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
        self.penalties = get_events_grouped_by_player(get_penalties(self, matches))
        self.top_scorers = get_events_grouped_by_player(self.goals_for)

    def __str__(self):
        return "Team name : {}" \
               "\nNumber of matches: {}" \
               "\nNumber of points for team: {}" \
               "\nnumber of goals scored: {}" \
               "\nNumber of goals conceeded: {}" \
               "\nnumber of goal scorers: {}" \
               "\nnumber of players with penalties: {}" \
               "\n\nScorers: {}" \
               "\n\nAssists: {}" \
               "\n\nPenalties: {}" \
            .format(self.team_name,
                    len(self.matches),
                    find_number_of_points(self, self.matches),
                    len(self.goals_for), len(self.goals_against),
                    len(self.top_scorers), len(self.penalties),
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


def get_events_grouped_by_player(list_of_events):
    events = []
    for goal in list_of_events:
        events.append(goal.player)
    return Counter(events)


def get_assists_by_player(goals):
    assists = []
    for goal in goals:
        if goal.assist != "":
            assists.append(goal.assist)
    return Counter(assists)


def find_number_of_points(self, matches):
    points = 0
    for match in matches:
        if match.home_team == self.team_name:
            points += match.points_for_home
        else:
            points += match.points_for_away
    return points


def print_entries_sorted(match_events):
    s = ""
    for key, value in sorted(match_events.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        s += '\n' + key + ": " + str(value)
    return s.encode('utf-8')
