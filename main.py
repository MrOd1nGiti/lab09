from table import column_sums, diagonal_pattern, row_sums, transform


def main():
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)

    print(f"Исходная матрица: {matrix}")
    print(f"Суммы строк - {row_sums(matrix)}")
    print(f"Суммы столбцов - {column_sums(matrix)}")

    transformed = transform(matrix)
    print(f"Преобразованная матрица (вариант 1) - {transformed}")

    size = int(input("Введите размер для диагонального узора (>= 1): "))
    pattern = diagonal_pattern(size)
    print("Диагональный узор:")
    for row in pattern:
        print(*row)


if __name__ == "__main__":
    main()
