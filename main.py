import MapFileToObjects

import dto.Match as Match

directory = "goalFiles/"
file_names = MapFileToObjects.get_files_from_directory(directory)

for file_name in sorted(file_names):
    match_info, goals, penalties = MapFileToObjects.get_data_from_file(directory + file_name)
    match = Match.Match(match_info, goals, penalties)
    print match
    print "****************************\n"

# todo pretty print goals and penalties so that different parameters are lined under each other