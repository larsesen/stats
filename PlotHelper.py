import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator


def plot_point_list_for_data(point_list, name):
    acc = np.cumsum(point_list)
    plt.figure().gca().yaxis.set_major_locator(MaxNLocator(integer=True))  # plot integers on y-axis
    x = xrange(len(point_list))
    plt.plot(x, acc)
    plt.title(name.decode('utf-8'))
    plt.xlabel("Number of matches in season")
    plt.ylabel("points (accumulated)")
    plt.show()
