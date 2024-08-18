def get_Permutation(n, k):
    def factorial(k):
        if k == 1 or k == 0:
            return 1
        else:
            return k * factorial(k - 1)
        
    available_nums = []
    for i in range(1, n + 1):
        available_nums.append(i)
    
    output_string = ""
    
    j = n
    m = k-1
    while j > 0:
        order = m // factorial(j-1)
        m  = m % factorial(j - 1)
        j -= 1
        output_string = output_string + str(available_nums.pop(order))
    
    return output_string

print(get_Permutation(5, 4))
