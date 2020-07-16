
dp_dict = {}
def uniquePaths(m: int, n: int) -> int:

    if m == 1 or n == 1:
        return 1
    if (m,n) in dp_dict:
        return dp_dict[(m,n)]
    elif (n,m) in dp_dict:
        return dp_dict[(n,m)]
    else:
        temp = uniquePaths(m,n-1) + uniquePaths(m-1,n)
        dp_dict[(m,n)] = temp
        dp_dict[(n,m)] = temp
        return temp

if __name__ == "__main__":
    print(uniquePaths(13,21))