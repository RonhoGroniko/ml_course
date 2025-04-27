import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = "student_scores.csv"

with open(file_path, 'r') as file:
    data = pd.read_csv(file)
print("Какой из входных столбцов выбрать в качестве Х? Введите Hours или Scores")
x = str(input())
if x == "Hours":
    first_column, second_column = data.columns[:2]
    y = "Scores"
else:
    second_column, first_column = data.columns[:2]
    y = "Hours"

hours = data[first_column].values
scores = data[second_column].values

max_hours = np.max(hours)
max_scores = np.max(scores)

min_hours = np.min(hours)
min_scores = np.min(scores)

avg_hours = np.mean(hours)
avg_scores = np.mean(scores)

print(f"Количество данных: {len(hours)}")
print("Столбец часов: ")
print(f"Max = {max_hours}, Min = {min_hours}, Avg = {avg_hours}")
print("Столбец баллов: ")
print(f"Max = {max_scores}, Min = {min_scores}, Avg = {avg_scores}")


def LSM(x, y):

    x = np.array(x)
    y = np.array(y)
    n = len(x)

    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x ** 2)
    sum_xy = np.sum(x * y)

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x ** 2)

    return a, b


fig, axs = plt.subplots(1, 3, figsize=(20, 8))  # 3 строки и 1 колонка

for i in range(3):
    axs[i].scatter(hours, scores, color='black')
    axs[i].set_xlabel(x)
    axs[i].set_ylabel(y)

a = LSM(hours, scores)[0]
b = LSM(hours, scores)[1]
regression_line = a * hours + b
for i in range(1, 3):
    axs[i].plot(hours, regression_line, color='red')


for i in range(len(hours)):
    axs[2].plot([hours[i], hours[i]], [scores[i], regression_line[i]], color='grey', linestyle='dotted')

plt.show()
