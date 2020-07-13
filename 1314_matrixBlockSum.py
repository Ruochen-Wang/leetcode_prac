from typing import List

def matrixBlockSum(mat: List[List[int]], K: int) -> List[List[int]]:
    row = len(mat)
    col = len(mat[0])
    # construct a matrix for DP that is [row+2K][col+2K] size
    dp_matrix = [[0 for n in range(col + (K << 1) + 1)] for m in range(row + (K << 1) + 1)]
    
    # preparation for accumulation
    r = K+1
    while r+K < len(dp_matrix):
        c = K+1
        while c+K < len(dp_matrix[0]):
            dp_matrix[r][c] = mat[r-K-1][c-K-1]
            c += 1
        r += 1
    #print(dp_matrix)

    # accumulation by row
    r = 0
    while r < len(dp_matrix):
        c = 1
        while c < len(dp_matrix[0]):
            dp_matrix[r][c] += dp_matrix[r][c-1]
            c += 1
        r += 1
    #print(dp_matrix)

    # accumulation by col
    c = 0
    while c < len(dp_matrix[0]):
        r = 1
        while r < len(dp_matrix):
            dp_matrix[r][c] += dp_matrix[r-1][c]
            r += 1
        c += 1
    #print(dp_matrix)

    # cal sum
    res = [[0 for n in range(col)] for m in range(row)]
    r = K+1
    while r < len(dp_matrix)-K:
        c = K+1
        while c < len(dp_matrix[0])-K:
            # NOTE: block [r-K][c-K] is subtracted twice so we need to add it back
            res[r-K-1][c-K-1] = dp_matrix[r+K][c+K] - dp_matrix[r-K-1][c+K] - dp_matrix[r+K][c-K-1] + dp_matrix[r-K-1][c-K-1]
            c += 1
        r += 1

    return res


if __name__ == "__main__":
    mat = [[1,2,3,1],[4,5,6,1],[7,8,9,1]]
    print(matrixBlockSum(mat, 1))