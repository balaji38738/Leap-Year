import matplotlib.pyplot as plt

odd = [1, 3, 5, 7]
odd_square = [1, 9, 25, 49]
even = [2, 4, 6, 8]
even_square = [4, 16, 36, 64]
plt.bar(odd, odd_square, label='bar1', color='c')
plt.bar(even, even_square, label='bar2', color='b')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('bar graph')
plt.legend()
plt.show()