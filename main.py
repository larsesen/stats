import MapFileToObjects

import dto.Match as Match

directory = "goalFiles/"
file_names = MapFileToObjects.get_matches_from_directory(directory)

for file_name in file_names:
    goals, match_info = MapFileToObjects.get_goals_from_file(directory + file_name)
    match = Match.Match(match_info.home_team, match_info.away_team, goals)
    print match_info
    print match
    print "\n"
