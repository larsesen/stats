#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MapFileToObjects
import ExtractStatistics as Stats
import PlotHelper as Plotter
import PrettyPrint as Print
import dto.Season as Season

directory = "../match_reports/"
file_names = MapFileToObjects.get_files_from_directory(directory)


matches = Stats.get_all_matches(directory, file_names)
season = Season.Season("BMIL", matches)
print season

#data_for_season = Stats.get_all_season_data(matches)

# todo does not work when team_name contains non-ascii. Fix...
team_name = 'BMIL'
matches_for_team = Stats.get_matches_for_team(matches, team_name)

# plots points for team
points_for_team = Stats.get_match_results_as_points(matches_for_team, team_name)
Plotter.plot_point_list_for_data(points_for_team, team_name)

#plots points per player
#name = 'Tom Egil Arnesen'
#point_list = Stats.get_points_per_game_for_player(matches_for_team, name)
#Plotter.plot_point_list_for_data(point_list, name)

# todo Plot all teams in same graph with different colors?
# todo make this file run interactively, by selecting team and then player to show stats for?