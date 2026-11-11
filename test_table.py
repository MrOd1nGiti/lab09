from table import column_sums, diagonal_pattern, row_sums, transform

matrix_test = [[1, 2, 3], [4, 5, 6]]
assert row_sums(matrix_test) == [6, 15]
assert column_sums(matrix_test) == [5, 7, 9]

assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]

assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]

assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

expected_pattern_3 = [[0, 1, 1], [2, 0, 1], [2, 2, 0]]
assert diagonal_pattern(3) == expected_pattern_3

control_matrix = [[-2, 0, 3], [4, -5, 6]]
control_copy = [row.copy() for row in control_matrix]
expected_transformed_v1 = [[0, 0, 3], [4, 0, 6]]

result = transform(control_matrix)
assert result == expected_transformed_v1
assert control_matrix == control_copy

result[0][0] = 99
assert control_matrix[0][0] == -2

print("Все проверки для работы 9 успешно пройдены")
