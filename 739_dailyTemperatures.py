# use a stack to keep the previous warmer day
def dailyTemperatures(T):
    stack = []
    warmer_day = [0]
    day = len(T)-1
    stack.append((T.pop(), day))
    while len(T) != 0:
        temp = T.pop()
        day -= 1
        
        # pop till find a warmer day
        while len(stack) > 0 and temp >= stack[-1][0]:
            stack.pop()
            
        # a local warmer day    
        if len(stack) == 0:
            stack.append((temp, day))
            warmer_day = [0] + warmer_day
        # find a warmer day
        else:
            warmer_day = [stack[-1][1] - day] + warmer_day
            stack.append((temp, day))
    
    return warmer_day

if __name__ == "__main__":
    temp = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(temp))