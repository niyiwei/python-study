#使用scatter绘制散点图并设置样式
import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, s=40)
# plt.scatter(x_values, y_values, c = 'red', edgecolor='none', s=40)
#使用颜色映射，从起始颜色渐变到结束颜色
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor='none', s=40)

plt.title("Square Numbers", fontsize = 24)

plt.xlabel("Value", fontsize = 14)

plt.ylabel("Square of Value", fontsize = 14)

#设置刻度标记的大小
plt.tick_params(axis = "both", which = "major", labelsize = 14)

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()

#保存图片，跟show方法只能调用一个
plt.savefig('D://squares_plot.png', bbox_inches='tight')