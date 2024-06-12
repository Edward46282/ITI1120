def longest_run(lenlist):
    '''
    (list of numbers) -> int
    This function takes a list of numbers and it returns the length of the longest run. 
    '''
    longtracker = 1
    curre = 1
    if len(lenlist) == 0:
        return 0
    for i in range(0,len(lenlist)-1):
        if lenlist[i] == lenlist[i+1]:
            curre += 1

        elif lenlist[i] != lenlist[i+1]:
            if longtracker < curre:
                longtracker = curre
            else:
                curre = 1
        if i == len(lenlist)-2:
            if longtracker < curre:
                longtracker = curre
    return longtracker


#main
usin = input("Please input a list of numbers seperated by space:\t").strip().split()
new_usin = []
for h in usin:
    h = float(h)
    new_usin.append(h)
print(longest_run(new_usin))
