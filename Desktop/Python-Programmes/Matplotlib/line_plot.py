import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6], label='first line', color='r')
plt.plot([7, 8, 9], [49, 64, 81], label='second line', color="b")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('line graph')
plt.legend()
plt.show()
