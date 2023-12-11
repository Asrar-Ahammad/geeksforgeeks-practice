def longestPrefix(strs):
    min_str = min(len(a) for a in strs)
    string = ''
    for i in range(min_str):
        key = strs[0][i]
        for item in strs:
            if (item[i] != key):
                if string == '':
                    return -1
                return string
        string += key
    return string


arr = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
print(longestPrefix(arr))
