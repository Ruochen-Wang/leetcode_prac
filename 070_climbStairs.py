def climbStairs(n: int) -> int:
    prevprev = 1
    prev = 2
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(n-2):
            curr = prevprev + prev
            prevprev = prev
            prev = curr
    return curr

if __name__ == "__main__":
    print(climbStairs(10))
    