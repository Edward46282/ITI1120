def squarefree(s):
    num_of_ch = len(s)
    for i in range(1,num_of_ch // 2+1):
        for ac in range(num_of_ch - 2*i+1):
            if s[ac:ac + i] == s[ac + i:ac + 2 * i]:
                return False
    return True
