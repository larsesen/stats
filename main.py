import RetrieveDataFromFile
import dto.Match

from PlotHistogram import get_plot


def get_goal_timestamps():
    return RetrieveDataFromFile.get_goal_timestamps_for_match()


#TODO: Clean names and variables into methods
goal_timestamps = dto.Match.get_goal_time_in_seconds(get_goal_timestamps())
plot = get_plot(goal_timestamps)
plot.show()
