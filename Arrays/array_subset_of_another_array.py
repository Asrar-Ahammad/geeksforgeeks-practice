def isSubset(a1, a2, n, m):
    dict1 = {}
    dict2 = {}

    for i in a1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    for i in a2:
        if i not in dict2:
            dict2[i] = 1
        else:
            dict2[i] += 1
    # print(dict1)
    # print(dict2)

    for i in dict2:
        if i in dict1:
            if dict2[i] <= dict1[i]:
                continue
            else:
                return "No"
        else:
            return "No"
    return "Yes"

    # a1 = set(a1)
    # a2 = set(a2)
    #
    # a3 = a1.intersection(a2)
    #
    # if len(a3) == len(a2):
    #     return "Yes"
    # else:
    #     return "No"
# a1 = [1, 2, 3, 4, 4, 5, 6]
# a2 = [1, 2, 4]
a1 = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8]
a2 = [1, 2 ,3 ,1]
# a1 = [10, 5, 2, 23, 19]
# a2 = [19, 5, 3]

n = len(a1)
m = len(a2)

print(isSubset(a1,a2,n,m))