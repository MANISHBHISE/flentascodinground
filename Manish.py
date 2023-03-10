def canMakeStr2(s1, s2):
    # Create a count array and count
    # frequencies characters in s1
    count = {s2[i]: 0 for i in range(len(s2))}

    for i in range(len(s2)):
        count[s2[i]] += 1

    # Now traverse through str2 to check
    # if every character has enough counts
    for i in range(len(s1)):
        if (count.get(s1[i]) == None or count[s1[i]] == 0):
            return False
        count[s1[i]] -= 1
    return True


# Driver Code


t = int(input())

if (t >= 1 and t <= 100):
    for t in range(t):
        s1 = str(input())
        s2 = str(input())
        if canMakeStr2(s1, s2):
            print("YES")
        else:
            print("NO")
