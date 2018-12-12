#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

base_url = "https://wp.nif.no/PageMatchWithResult.aspx?LinkId="
match_id = "6861087"

f = urllib.urlopen(base_url + match_id)
my_file = f.read()

last_part = my_file.split('var teamVM = \'')[1]
team_vm = my_file.split('var teamVM = \'')[1].split('\n')[0]


def get_variable_from_file(variable_name):
    return last_part.split(variable_name)[1].split("\n")[0]


def get_contents_with_brackets(headline, variable):
    string = "\"{}\": [".format(headline)
    string += variable[:-3]
    string += "],"
    return string


match_info = get_variable_from_file('var matchBasicInfoVM = \'')
match_statistics = get_variable_from_file('var matchStatistics = \'')
goals_in_order = get_variable_from_file('var goalsInOrderVM = \'')
match_penalties = get_variable_from_file('var matchPenaltiesVM = \'')

all_info = "{"
all_info += get_contents_with_brackets("teams", team_vm)
all_info += get_contents_with_brackets("match_info", match_info)
all_info += get_contents_with_brackets("match_statistics", match_statistics)
all_info += get_contents_with_brackets("goals_in_order", goals_in_order)
all_info += get_contents_with_brackets("match_penalties", match_penalties)

all_info = all_info[:-1] # removing last comma
all_info += "}"

print all_info

# todo
# Save file to directory
# Add support for several files (matches)
# Extract data from file using existing parsers
