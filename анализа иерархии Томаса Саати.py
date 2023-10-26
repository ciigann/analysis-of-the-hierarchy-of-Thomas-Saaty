from colorama import Style


def get_weights(num_criteria):
    # Создаем матрицу размером num_criteria x num_criteria
    matrix = [[0 for _ in range(num_criteria)] for _ in range(num_criteria)]

    # Вводим веса попарного сравнения критериев
    for i in range(num_criteria):
        for j in range(num_criteria):
            if i == j:
                # Элементы главной диагонали всегда равны 1
                matrix[i][j] = 1
            elif j < i:
                # Если уже ввели вес для пары (j, i), то используем его
                matrix[i][j] = 1 / matrix[j][i]
            else:
                weight = 0
                while weight == 0:
                    try:  # что бы проверить является ли введенная строка числом попробуем преобразовать ее в float и будем ловить исключение
                        weight = float(input(f"Введите вес для пары ({i}, {j}): "))
                        if weight < 0:  # проверим является ли введенное число положительным
                            weight = 0
                            print('\033[31m',
                                  'вес для пары должно быть задан положительным числом!!!' + Style.RESET_ALL)
                    except ValueError:  # ловим исключение при ошибке
                        print('\033[31m', 'вес для пары должно быть задан числом!!!' + Style.RESET_ALL)
                        weight = 0
                        pass
                matrix[i][j] = weight

    # Вычисляем весовые коэффициенты
    weights = [1 for _ in range(num_criteria)]
    for i in range(num_criteria):
        for j in range(num_criteria):
            weights[i] *= matrix[i][j]
        # Корень num_criteria-ой степени
        weights[i] **= 1 / num_criteria

    # Нормализуем веса
    total = sum(weights)
    normalized_weights = [round(weight / total, 2) for weight in weights]

    return normalized_weights


# Вводим количество критериев
num_criteria = 0
while num_criteria == 0:
    try:  # что бы проверить является ли введенная строка числом попробуем преобразовать ее в int и будем ловить исключение
        num_criteria = int(input("Введите количество критериев: "))
        if num_criteria < 0:  # проверим является ли введенное число положительным
            num_criteria = 0
            print('\033[31m', 'Количество критериев должно быть задано положительным числом!!!' + Style.RESET_ALL)
    except ValueError:  # ловим исключение при ошибке
        print('\033[31m', 'Количество критериев должно быть задано целым числом!!!' + Style.RESET_ALL)
        num_criteria = 0
        pass
weights = get_weights(num_criteria)

# Выводим весовые коэффициенты
print("\033[1m" "\nВесовые коэффициенты:" + Style.RESET_ALL)
for weight in weights:
    print(f"Весовой коэффициент: {weight:.2f}")