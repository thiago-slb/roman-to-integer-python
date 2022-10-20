def romanToInt(s: str) -> int:
    nDict = {
        "I":             1,
        "V":             5,
        "X":             10,
        "L":             50,
        "C":             100,
        "D":             500,
        "M":             1000
    }
    
    sLen = len(s)
    x = sLen - 1
    
    response = 0
    
    while x >= 0:
        if x < sLen-1 and nDict[s[x]] < nDict[s[x+1]]:
            response -= nDict[s[x]]
        else:
            response += nDict[s[x]]
        x-=1
        
    return response