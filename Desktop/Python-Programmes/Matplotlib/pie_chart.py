import matplotlib.pyplot as plot
slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']
plot.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        explode=(0, 0.1, 0, 0),
        autopct='%.2f%%',
        shadow=True,
        )
plot.show()
