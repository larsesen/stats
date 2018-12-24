#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
from Helper import MatchResult as MatchResult


class Season(object):
    team_name = ""
    matches = []
    goals_for = []
    goals_against = []
    assists = []
    penalties = []
    top_scorers = []
    match_results = []

    def __init__(self, team_name, matches):
        self.team_name = team_name
        self.matches = matches
        self.goals_for = get_goals_for(self, matches)
        self.goals_against = get_goals_against(self, matches)
        self.top_scorers = get_events_grouped_by_player(self.goals_for)
        self.assists = get_assists_by_player(self.goals_for)
        self.penalties = get_events_grouped_by_player(get_penalties(self, matches))
        self.match_results = get_match_results_for_team(self, matches)

    def __str__(self):
        return "Team name : {}" \
               "\nNumber of matches played: {}" \
               "\nNumber of full time wins: {}" \
               "\nNumber of penalty wins: {}" \
               "\nNumber of penalty losses: {}" \
               "\nNumber of full time losses: {}" \
               "\nnumber of goals scored: {}" \
               "\nNumber of goals conceded: {}" \
               "\nGoal Differential: {}" \
               "\nNumber of points for team: {}" \
               "\n\n\nnnumber of goal scorers: {}" \
               "\nnumber of players with penalties: {}" \
               "\n\nScorers: {}" \
               "\n\nAssists: {}" \
               "\n\nPenalties: {}" \
            .format(self.team_name,
                    len(self.matches),
                    get_number_of_occurrences(self.match_results, MatchResult.WIN),
                    get_number_of_occurrences(self.match_results, MatchResult.WIN_PEN),
                    get_number_of_occurrences(self.match_results, MatchResult.LOSS_PEN),
                    get_number_of_occurrences(self.match_results, MatchResult.LOSS),

                    len(self.goals_for), len(self.goals_against),
                    len(self.goals_for) - len(self.goals_against),
                    len(self.top_scorers), len(self.penalties),
                    find_number_of_points(self.match_results),
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


def get_opposite(result_for_home_team):
    if result_for_home_team == MatchResult.WIN:
        return MatchResult.LOSS
    if result_for_home_team == MatchResult.WIN_PEN:
        return MatchResult.LOSS_PEN
    if result_for_home_team == MatchResult.LOSS_PEN:
        return MatchResult.WIN_PEN
    if result_for_home_team == MatchResult.LOSS:
        return MatchResult.WIN


def get_match_results_for_team(self, matches):
    results = []
    for match in matches:
        if match.home_team == self.team_name:
            results.append(match.result_for_home_team)
        else:
            results.append(get_opposite(match.result_for_home_team))
    return results


def find_number_of_points(results):
    points = 0
    for result in results:
        if result == MatchResult.WIN:
            points += 3
        elif result == MatchResult.WIN_PEN:
            points += 2
        elif result == MatchResult.LOSS_PEN:
            points += 1
    return points


def get_number_of_occurrences(match_results, final_result):
    occurrences = 0
    for result in match_results:
        if result == final_result:
            occurrences += 1
    return occurrences


def print_entries_sorted(match_events):
    s = ""
    for key, value in sorted(match_events.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        s += '\n' + key + ": " + str(value)
    return s.encode('utf-8')
