def convert_to_base(num, base):
    # если число равно 0
    if num == 0:
        return ""
    
    # Получаем остаток от деления, чтобы определить текущую цифру
    remainder = num % base
    # Если остаток больше 9, используем буквенные обозначения
    if remainder >= 10:
        digit = chr(ord('A') + remainder - 10)  # Преобразуем число в букву
    else:
        digit = str(remainder)
    
    # Рекурсивно вызываем функцию для целочисленного деления
    return convert_to_base(num // base, base) + digit

# Подставляем число которое будем переводить и систему в которую будем переводить
number = 28  # Число для перевода
base = 3  # Система счисления (от 2 до 16)
result = convert_to_base(number, base)

# Печать результата
print(f"Число {number} в системе счисления с основанием {base} равно {result}")