import matplotlib.pyplot as plt


def getPlot(goals):
    #TODO: Configure plot with axis. See https://stackoverflow.com/questions/30886364/plotting-a-histogram-from-array
    plt.hist(goals,bins=[1 , 2 , 3 , 4 , 5])
    return plt