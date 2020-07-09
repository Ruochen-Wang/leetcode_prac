

def countBits(num: int):
        res = [0]
        loop = 1
        i = 1
        while i <= num:
            if i == loop << 1:
                loop = loop << 1
            res.append(res[i%loop]+1)
            i += 1
        return res

if __name__ == "__main__":
    print(countBits(20))