from ReadFile import read_json_data

from dto.Match import make_timestamp_in_match
from dto.Period import makeTimeInPeriod

from GoalConstants import GoalAccessObjects

import RetrieveDataFromFile

BMIL = "BMIL Herrer 1"


def get_goal_timestamps_for_match():
    # TODO: Traverse all files in directory "goalFiles"
    # TODO: Object with goals is contained in object named goalsInOrderVM. Provide only linkid from main for result page and retrieve automatically

    first = RetrieveDataFromFile.get_timestamps_from_file("goalFiles/20180916_lyn_bmil.json")
    second = RetrieveDataFromFile.get_timestamps_from_file("goalFiles/20180922_bmil_grei.json")
    third = RetrieveDataFromFile.get_timestamps_from_file("goalFiles/20180930_lsk_bmil.json")

    fourth = RetrieveDataFromFile.get_timestamps_from_file("goalFiles/20181003_bmil_ajer.json")
    fifth = RetrieveDataFromFile.get_timestamps_from_file("goalFiles/20181014_ullkisa_bmil.json")
    sixth = RetrieveDataFromFile.get_timestamps_from_file("goalFiles/20181027_bmil_oreasen.json")

    seventh = RetrieveDataFromFile.get_timestamps_from_file("goalFiles/20181104_vif_bmil.json")
    eighth = RetrieveDataFromFile.get_timestamps_from_file("goalFiles/20181117_bmil_lyn.json")
    ninth = RetrieveDataFromFile.get_timestamps_from_file("goalFiles/20181124_grei_bmil.json")

    all_goals = first + second + third + fourth + fifth + sixth + seventh + eighth + ninth

    print "\nTotal of {} goals scored".format(len(all_goals))

    return all_goals


def get_timestamps_from_file(path):
    first = read_json_data(path)
    timestamps_second = get_timestamps_in_match(first)
    return timestamps_second


def get_timestamps_in_match(data):
    timestamps = []
    for goal in data:
        if goal[GoalAccessObjects.TeamName] == BMIL:
            timestamps.append(create_match_timestamp(goal))
    return timestamps


def get_timestamps_in_period(data):
    timestamps = []
    for goal in data:
        if goal[GoalAccessObjects.TeamName] == BMIL:
            match_timestamp = create_match_timestamp(goal)
            timestamps.append(makeTimeInPeriod(match_timestamp.minutes, match_timestamp.seconds))
    return timestamps


def create_match_timestamp(goal):
    time = goal[GoalAccessObjects.Time]

    if time == "Str": #no timestamp for penalty shootout
        return
    time_and_period = time.split("-")
    period = int(time_and_period[0])
    minutes_and_seconds = time_and_period[1].strip().split(':')
    timestamp = make_timestamp_in_match(period, minutes_and_seconds[0], minutes_and_seconds[1])
    return timestamp
