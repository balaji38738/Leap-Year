import matplotlib.pyplot as plot

odd = [1, 3, 5, 7]
odd_square = [1, 9, 25, 49]
even = [2, 4, 6, 8]
even_square = [4, 16, 36, 64]
plot.bar(odd, odd_square, label='bar1', color='c')
plot.bar(even, even_square, label='bar2', color='b')
plot.xlabel('x-axis')
plot.ylabel('y-axis')
plot.title('bar graph')
plot.legend()
plot.show()
