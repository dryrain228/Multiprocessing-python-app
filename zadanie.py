import multiprocessing
from PIL import Image, ImageDraw
import random
import numpy as np
import pyperclip


# Размер изображения
width, height = 800, 600

# Создаем пустое изображение
image = Image.new("RGB", (width, height), "white")

# Создаем объект ImageDraw для рисования на изображении
draw = ImageDraw.Draw(image)

# Функция для генерации случайных координат
def random_coordinates():
    return (random.randint(0, width), random.randint(0, height))

# Функция для рисования случайной фигуры
def draw_random_shape():
    position = random_coordinates()
    shape_type = random.choice(["circle", "square", "triangle"])
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if shape_type == "circle":
        radius = random.randint(20, 100)
        draw.ellipse((position[0] - radius, position[1] - radius, position[0] + radius, position[1] + radius), fill=color)
    elif shape_type == "square":
        size = random.randint(20, 100)
        draw.rectangle((position[0], position[1], position[0] + size, position[1] + size), fill=color)
    elif shape_type == "triangle":
        vertices = [position]
        for _ in range(2):
            vertices.append(random_coordinates())
        draw.polygon(vertices, fill=color)
# Рисуем случайные фигуры
for _ in range(10):  # Нарисовать 10 случайных фигур
    draw_random_shape()
# Сохраняем изображение
image.save("random_shapes.png")

def process_two_work():
    np_matrix = np.random.randint(-10, 10, size=(5, 5))
    sum_negative_odd_rows = sum(np_matrix[i, j] for i in range(5) for j in range(5) if i % 2 != 0 and np_matrix[i, j] < 0)
    column_sums = np.sum(np_matrix, axis=0)
    columns_without_negatives = [i for i, col_sum in enumerate(column_sums) if all(np_matrix[:, i] >= 0)]
    sum_columns_without_negatives = sum(column_sums[columns_without_negatives])

    with open('output.txt', 'w') as f:
        f.write("Matrix:\n")
        f.write(str(np_matrix))
        f.write("\nСумма отрицательных элементов в нечетных рядах: " + str(sum_negative_odd_rows))
        f.write("\nСумма элементов в столбцах без отрицательных элементов: " + str(sum_columns_without_negatives))


if __name__ == "__main__":
    # Создаем процессы
    draw_process = multiprocessing.Process(target=draw_random_shape)
    process_two = multiprocessing.Process(target=process_two_work)
    #process_three = multiprocessing.Process(target=generate_password, args=(password_length, include_uppercase))

    # Запускаем процессы
    draw_process.start()
    process_two.start()
    #process_three.start()

    # Дожидаемся завершения каждого процесса
    draw_process.join()
    process_two.join()
    #process_three.join()
