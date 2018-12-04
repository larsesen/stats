import MapFileToObjects

import dto.Match as Match

directory = "goalFiles/"
file_names = MapFileToObjects.get_matches_from_directory(directory)

for file_name in file_names:
    goals = MapFileToObjects.get_goals_from_file(directory + file_name)
    match = Match.Match("home", "away", goals)
    print match

