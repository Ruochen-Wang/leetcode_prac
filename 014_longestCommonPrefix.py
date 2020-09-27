from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]
    elif len(strs) == 2:
        shorter = len(strs[0]) if (len(strs[0]) < len(strs[1])) else len(strs[1])
        i = 0
        while i < shorter and strs[0][i] == strs[1][i]:
            i += 1
        return strs[0][0:i]
    else: 
        return longestCommonPrefix([longestCommonPrefix(strs[0:len(strs)//2]), longestCommonPrefix(strs[len(strs)//2:len(strs)])])


if __name__=="__main__":
    strs = ["flower","flow","floght"]
    strs = ["fafaf"]
    print(longestCommonPrefix(strs))