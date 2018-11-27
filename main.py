import StatsUtil

from PlotHistogram import get_plot

goals = StatsUtil.get_goal_timestamps()
goal_timestamps = StatsUtil.get_goal_time_in_seconds(goals)

StatsUtil.print_timestamps(goal_timestamps)

plot = get_plot(goal_timestamps)
plot.show()
