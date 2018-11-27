import matplotlib.pyplot as plt


def get_plot(goals):

    # define window size, output and axes
    fig, ax = plt.subplots(figsize=[6, 6])

    # set plot title
    ax.set_title("Timestamp of goals scored")

    # set x-axis name
    ax.set_xlabel("Number of seconds")

    # set y-axis name
    ax.set_ylabel("Number of goals")


    # create histogram within output
    N, bins, patches = ax.hist(goals, bins=60, color="#777777")  # initial color of all bins

    return plt
