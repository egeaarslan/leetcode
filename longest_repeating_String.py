def lengthOfLongestSubstring(s):
    vault = []
    if s:
        res = 1
    else:
        return 0
    
    count = 0
    for char in s:
        if char in vault:
            # Instead of resetting, remove characters from the start until the duplicate is gone
            vault = vault[vault.index(char) + 1:]
            count = len(vault)
        
        count += 1
        vault.append(char)

        if count > res:
            res = count

    return res

print(lengthOfLongestSubstring("dvdf"))
