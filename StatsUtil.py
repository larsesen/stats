import RetrieveDataFromFile


def get_goal_timestamps():
    return RetrieveDataFromFile.get_goal_timestamps_for_match()


def get_goal_time_in_seconds(goals):
    timestamps_in_seconds = []
    for goal in goals:
        if goal is not None:
            period_number = goal.get_period()
            minutes = goal.get_minutes()
            seconds = goal.get_seconds()

            time_in_seconds = get_time_of_match_from_period_number(period_number) \
                              + get_minutes_as_seconds(minutes) + int(seconds)

            timestamps_in_seconds.append(time_in_seconds)
    timestamps_in_seconds.sort()
    return timestamps_in_seconds


def get_minutes_as_seconds(minutes):
    return int(minutes) * 60


def get_time_of_match_from_period_number(period):
    return (int(period) - 1) * 20 * 60


def print_timestamps(timestamps):
    for timestamp in timestamps:
        if timestamp is not None:
            print timestamp
