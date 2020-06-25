import matplotlib.pyplot as plt
from matplotlib import animation, style
#use style.available to print all graph style options
#can pass a list of styles as well
style.use('Solarize_Light2')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#Plots animated graph
def animate(i):
    file = open('example.txt', 'r').read()
    lines = file.split('\n')
    xs, ys = [], []
    for line in lines:
        x, y = line.split(',')
        xs.append(int(x))
        ys.append(int(y))
    ax.clear()
    ax.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
