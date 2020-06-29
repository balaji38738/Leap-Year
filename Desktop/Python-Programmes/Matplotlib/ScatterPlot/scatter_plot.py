import matplotlib.pyplot as plt

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_cube = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
plt.scatter(nums, nums_cube, label='cubic graph', s=200, marker='+')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('scatter plot')
plt.legend()
plt.show()
