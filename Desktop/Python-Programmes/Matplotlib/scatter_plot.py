import matplotlib.pyplot as plot

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_cube = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
plot.scatter(nums, nums_cube, label='cubic graph', s=200, marker='+')
plot.xlabel('x-axis')
plot.ylabel('y-axis')
plot.title('scatter plot')
plot.legend()
plot.show()
