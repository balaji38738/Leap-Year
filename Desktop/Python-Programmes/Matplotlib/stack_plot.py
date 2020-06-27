import matplotlib.pyplot as plot

days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]
plot.plot([], [], color='r', label='sleeping', linewidth=5)
plot.plot([], [], color='b', label='eating', linewidth=5)
plot.plot([], [], color='c', label='working', linewidth=5)
plot.plot([], [], color='k', label='playing', linewidth=5)
plot.stackplot(days, sleeping, eating, working, playing, colors=['r', 'b', 'c', 'k'])
plot.legend()
plot.show()
