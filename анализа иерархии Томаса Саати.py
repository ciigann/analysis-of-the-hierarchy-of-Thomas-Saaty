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
                weight = float(input(f"Введите вес для пары ({i}, {j}): "))
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
num_criteria = int(input("Введите количество критериев: "))
weights = get_weights(num_criteria)

# Выводим весовые коэффициенты
print("Весовые коэффициенты:")
for weight in weights:
    print(f"Весовой коэффициент: {weight:.2f}")