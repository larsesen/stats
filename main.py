import MapFileToObjects

import dto.Match as Match

directory = "goalFiles/"
file_names = MapFileToObjects.get_files_from_directory(directory)

matches = []
for file_name in sorted(file_names):
    match_info, goals, penalties = MapFileToObjects.get_data_from_file(directory + file_name)
    match = Match.Match(match_info, goals, penalties)
    matches.append(match)


for match in matches:
    print match