def isNumber(s):
    after_e = False
    after_dot = False
    for i in range(len(s)):
        if i == 0:
            if s[i] == "-" or s[i] == "+" or s[i] == ".":
                if s[i] == ".":
                    if len(s) == 1:
                        return False
                    if s[i+1] == "e" or s[i+1] == "E":
                        return False
                    after_dot = True
                else:
                    if i == len(s) -1:
                        return False
                    if s[i+1] == "." and i+2 == len(s):
                        return False
                    if s[i+1] == "E" or s[i+1] == "e":
                        return False
                    if s[i+1] == "." and (s[i+2] == "E" or s[i+2] == "e"):
                        return False
                    

            else:
                try:
                    int(s[i])
                except:
                    return False
                
        elif after_e == True:
            if i == j:
                if s[i] == "+" or s[i] == "-":
                    if i == len(s) -1:
                        return False
                    continue
                else:
                    try:
                        int(s[i])
                    except:
                        return False
            else:
                try:
                    int(s[i])
                except:
                    return False

        elif after_dot == True:
            if s[i] == "e" or s[i] == "E":
                after_e = True
                j = i+1
                if j >= len(s):
                    return False
            else:
                try:
                    int(s[i])
                except:
                    return False
                
        
        else:
            if s[i] == "e" or s[i] == "E" or s[i] == ".":
                if s[i] == "e" or s[i] == "E":
                    after_e = True
                    j = i+1
                    if j >= len(s):
                        return False
                else:
                    after_dot = True 
            else:
                try:
                    int(s[i])
                except:
                    return False
    return True