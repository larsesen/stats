import MapFileToObjects

import dto.Match as Match

directory = "goalFiles/"
file_names = MapFileToObjects.get_files_from_directory(directory)

for file_name in file_names:
    match_info, goals = MapFileToObjects.get_data_from_file(directory + file_name)
    match = Match.Match(match_info, goals)
    print match
    print "\n"
