"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""

def solution(s):
    
    collector = []

    for i in range(0, len(s), 2):
        if (len(s)) % 2 == 0:
            collector.append(s[i] + s[i+1])
        else:
           s = s + "_"
           print(s)
           collector.append(s[i] + s[i+1])
    
    
    return collector

print(solution('abc'))
print(solution('abcdef'))
