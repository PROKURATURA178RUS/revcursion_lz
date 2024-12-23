def generate_permutations(lst):
    # если список пустой, возвращаем пустой список
    if len(lst) == 0:
        return [[]]
    
    # Рекурсия
    permutations = []  # Список для хранения перестановок
    for i in range(len(lst)):
        # Убираем текущий элемент и генерируем перестановки для оставшихся
        remaining = lst[:i] + lst[i+1:]
        for p in generate_permutations(remaining):
            # Добавляем текущий элемент к каждой перестановке
            permutations.append([lst[i]] + p)

    return permutations

# Список, перестановки которого и будем выводить
my_list = [1, 2, 3, 4, 5] 
result = generate_permutations(my_list)

# Вывод результата
for perm in result:
    print(perm)