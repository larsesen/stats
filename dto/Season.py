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

    def __init__(self, team_name, matches):
        self.team_name = team_name
        self.matches = get_matches_for_team(team_name, matches)
        self.goals_for = get_goals_for(self, self.matches)
        self.goals_against = get_goals_against(self, self.matches)
        self.assists = get_assists(self, self.matches)
        self.penalties = get_penalties(self, self.matches)

    def __str__(self):
        return '{text: <{width}}'.format(text=self.team_name, width=15) + \
               '{text: <{width}}'.format(text=len(self.matches), width=3) + \
               '{text: <{width}}'.format(
                   text=get_number_of_occurrences(self.get_match_results_for_team(), MatchResult.WIN), width=3) + \
               '{text: <{width}}'.format(
                   text=get_number_of_occurrences(self.get_match_results_for_team(), MatchResult.WIN_PEN),
                   width=3) + \
               '{text: <{width}}'.format(
                   text=get_number_of_occurrences(self.get_match_results_for_team(), MatchResult.LOSS_PEN),
                   width=3) + \
               '{text: <{width}}'.format(
                   text=get_number_of_occurrences(self.get_match_results_for_team(), MatchResult.LOSS),
                   width=3) + \
               '{text: <{width}}'.format(text=str(len(self.goals_for)) + '-' + str(len(self.goals_against)), width=6) + \
               '{text: <{width}}'.format(text=len(self.goals_for) - len(self.goals_against), width=4) + \
               '{text: <{width}}'.format(text=self.find_number_of_points(), width=4)

    def get_goals_grouped_by_player(self):
        events = []
        for event in self.goals_for:
            events.append(event.player)
        return Counter(events)

    def get_assists_by_player(self):
        return Counter(self.assists)

    def get_penalty_minutes_per_player(self):
        minutes_per_player = {}
        for entry in self.penalties:
            if entry.player not in minutes_per_player:
                minutes_per_player[entry.player] = entry.duration
            else:
                minutes_per_player[entry.player] += entry.duration
        return minutes_per_player

    def find_number_of_points(self):
        points = 0
        for result in self.get_match_results_for_team():
            if result == MatchResult.WIN:
                points += 3
            elif result == MatchResult.WIN_PEN:
                points += 2
            elif result == MatchResult.LOSS_PEN:
                points += 1
        return points

    def get_match_results_for_team(self):
        results = []
        for match in self.matches:
            if unicode(match.home_team).encode('utf-8') == self.team_name:
                results.append(match.match_info.result_for_home_team)
            elif unicode(match.away_team).encode('utf-8') == self.team_name:
                results.append(match.match_info.result_for_away_team)
            else:
                raise ValueError('Team must be either home or away')
        return results


def get_matches_for_team(team_name, matches):
    matches_for_team = []
    for match in matches:
        if unicode(match.home_team).encode('utf-8') == team_name or unicode(match.away_team).encode(
                'utf-8') == team_name:
            matches_for_team.append(match)
    return matches_for_team


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


def get_number_of_occurrences(match_results, final_result):
    occurrences = 0
    for result in match_results:
        if result == final_result:
            occurrences += 1
    return occurrences
