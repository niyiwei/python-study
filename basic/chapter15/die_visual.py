import pygal
from die import Die

#创建一个D6
die = Die()
die2 = Die()

#掷几次骰子，并将结构存储在一个列表中
results = []
for roll in range(1000):
	results.append(die.roll())


print(results)

#分析结果
frequencies = []

for value in range(1, die.num_sides + 1):
	frequencies.append(results.count(value))

print(frequencies)
print(results.count(1))

hist = pygal.Bar()

hist.title = "Resykts if rikkubg ibe D6 1000 times." 
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file("D://die_visual.svg")