#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MapFileToObjects
import ExtractStatistics as Stats
import PrettyPrint as Print

directory = "match_reports/"
file_names = MapFileToObjects.get_files_from_directory(directory)


matches = Stats.get_all_matches(directory, file_names)
data_for_season = Stats.get_all_season_data(matches)

timestamp_for_goals = Stats.get_timestamp_for_goals(data_for_season)
timestamp_for_penalties = Stats.get_timestamp_for_penalties(data_for_season)

Print.print_league_table(data_for_season)
