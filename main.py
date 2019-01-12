#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MapFileToObjects
import ExtractStatistics as Stats
import PlotHelper as Plotter
import PrettyPrint as Print


directory = "match_reports/"
file_names = MapFileToObjects.get_files_from_directory(directory)


matches = Stats.get_all_matches(directory, file_names)
data_for_season = Stats.get_all_season_data(matches)

timestamp_for_goals = Stats.get_timestamp_for_goals(data_for_season)
timestamp_for_penalties = Stats.get_timestamp_for_penalties(data_for_season)

#Print.print_league_table(data_for_season)

# todo does not work when team_name contains non-ascii. Fix...
team_name = 'Grei'
matches_for_team = Stats.get_matches_for_team(matches, team_name)

points_for_team = Stats.get_match_results_as_points(matches_for_team, team_name)
Plotter.plot_point_list_for_data(points_for_team, team_name)

#name = 'Thomas Bergsmark'
#point_list = Stats.get_points_per_game_for_player(matches_for_team, name)
#Plotter.plot_point_list_for_player(point_list, name)
