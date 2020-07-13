# WRONG ALGO!!
def maximalSquare(matrix) -> int:
    # use dp to remeber the previous solution
    row = len(matrix)
    col = len(matrix[0])
    edge_len = 1
    # construct a matrix for dp (1 extrafor edge handling)
    dp_matrix = [[0 for n in range(col+1)] for m in range(row+1)]
    i, j = 1, 1
    while i < row+1:
        j = 1
        while j < col+1:
            if matrix[i-1][j-1] == 1:
                dp_matrix[i][j] = min(dp_matrix[i][j-1], dp_matrix[i-1][j], dp_matrix[i-1][j-1])+1
                edge_len = max(dp_matrix[i][j], edge_len)
                print(dp_matrix)
            j += 1
        i += 1
    print(dp_matrix)
    return edge_len*edge_len

if __name__ == "__main__":
    # using 2 for convenience
    matrix = [[1,2,2,2,1],[2,1,1,1,1],[1,1,1,1,2],[1,1,1,1,1],[1,2,1,1,2]]
    print(maximalSquare(matrix))

