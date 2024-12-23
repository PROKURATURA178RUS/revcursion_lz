def pascal_triangle(n):
    #  если уровень 0, возвращаем треугольник с одной строкой
    if n == 0:
        return [[1]]
    
    # Рекурсивно строим треугольник для n-1 уровней
    triangle = pascal_triangle(n - 1)
    # Получаем последнюю строку
    last_row = triangle[-1]
    # Создаем новую строку, добавляя 1 в начале и в конце, и суммы элементов
    new_row = [1]  # Первая единица
    
    # Заполняем новую строку значениями
    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])
    
    new_row.append(1)  # Последняя единица
    triangle.append(new_row)  # Добавляем новую строку к треугольнику
    
    return triangle

# Количество уровней
n = 17  
triangle = pascal_triangle(n)

# Вывод треугольника Паскаля
for row in triangle:
    print(row)