#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MapFileToObjects
import ExtractStatistics as Stats
import dto.Season as Season
import PrettyPrint as Print


directory = "../match_reports/"
file_names = MapFileToObjects.get_files_from_directory(directory)

matches = Stats.get_all_matches(directory, file_names)
season = Season.Season("BMIL", matches)

Print.print_team_statistics(season)
