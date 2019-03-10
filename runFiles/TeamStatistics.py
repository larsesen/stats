#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MapFileToObjects
import ExtractStatistics as Stats
import PlotHelper as Plotter
import objects.Season as Season

directory = "../match_reports/"
file_names = MapFileToObjects.get_files_from_directory(directory)


matches = Stats.get_all_matches(directory, file_names)

# todo does not work when team_name contains non-ascii. Fix...
team_name = 'BMIL'
season = Season.Season(team_name, matches)
matches_for_team = Stats.get_matches_for_team(matches, team_name)


def get_matches_for_team(team_name):
    return Stats.get_matches_for_team(matches, team_name)


def print_graph_for_all_players_in_team():
    for player in season.get_players_and_number_of_matches_played().keys():
        point_list = Stats.get_points_per_game_for_player(matches_for_team, player)
        Plotter.plot_point_list_for_data(point_list, player)


def print_players_in_same_graph(top_scorers):
    point_lists = {}
    for player in top_scorers:
        point_list = Stats.get_points_per_game_for_player(matches_for_team, player)
        point_lists[player] = point_list
    Plotter.plot_graphs_in_same_figure(point_lists)


def plot_points_for_single_team():
    points_for_team = Stats.get_match_results_as_points(matches_for_team, team_name)
    Plotter.plot_point_list_for_data(points_for_team, team_name)


def plot_points_per_player(player_name):
    player_name = 'Tom Egil Arnesen'
    point_list = Stats.get_points_per_game_for_player(matches_for_team, player_name)
    Plotter.plot_point_list_for_data(point_list, player_name)


def plot_team_points_in_same_graph():
    team_names = ['Lyn','BMIL','Lillestrøm','Vålerenga']
    point_lists = {}
    for team in team_names:
        points_for_team = Stats.get_match_results_as_points(get_matches_for_team(team), team)
        point_lists[team] = points_for_team
    Plotter.plot_graphs_in_same_figure(point_lists)


plot_team_points_in_same_graph()
#print_graph_for_all_players_in_team()

#plot_team_points_in_same_graph(matches)

#top_scorers = ['Bendik Fürst Mustad', 'Thomas Bergsmark', 'Aksel Tjøtta Stenvold', 'Emil Varre Sandøy']
#print_players_in_same_graph(top_scorers)

#plot_points_for_single_team()

exit()