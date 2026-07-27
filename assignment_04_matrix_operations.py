# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter element [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    for row in matrix:
        print("".join(f"{value:5}" for value in row))


def transpose_matrix(matrix, rows, cols):
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def add_matrices(a, b, rows, cols):
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result


def multiply_matrices(a, b, m, n, p):
    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result


def main():
    print("PART A - Transpose a Matrix")
    rows_a = int(input("Enter number of rows: "))
    cols_a = int(input("Enter number of columns: "))

    matrix_a = read_matrix(rows_a, cols_a)
    transposed = transpose_matrix(matrix_a, rows_a, cols_a)

    print("\nOriginal Matrix:")
    display_matrix(matrix_a)
    print("\nTransposed Matrix:")
    display_matrix(transposed)

    print("\nPART B - Add Two Matrices")
    rows_b = int(input("Enter number of rows: "))
    cols_b = int(input("Enter number of columns: "))

    print("Enter first matrix:")
    matrix_b1 = read_matrix(rows_b, cols_b)
    print("Enter second matrix:")
    matrix_b2 = read_matrix(rows_b, cols_b)

    sum_result = add_matrices(matrix_b1, matrix_b2, rows_b, cols_b)

    print("\nSum Matrix:")
    display_matrix(sum_result)

    print("\nPART C - Multiply Two Matrices")
    m = int(input("Enter rows of Matrix A (M): "))
    n = int(input("Enter columns of Matrix A (N): "))
    n2 = int(input("Enter rows of Matrix B (must equal N): "))
    p = int(input("Enter columns of Matrix B (P): "))

    if n != n2:
        print("Error: Columns of A must equal rows of B.")
        return

    print("Enter Matrix A:")
    matrix_c1 = read_matrix(m, n)
    print("Enter Matrix B:")
    matrix_c2 = read_matrix(n, p)

    product_result = multiply_matrices(matrix_c1, matrix_c2, m, n, p)

    print("\nProduct Matrix (A x B):")
    display_matrix(product_result)


if __name__ == "__main__":
    main()
