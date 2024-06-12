def two_length_run(listing):
    '''
    (list of numbers) -> bool
    This function returns True if there are at least two numbers that are equal and come one after another. Otherwise, returns False
    '''
    for i in range(0,len(listing)-1):
        if listing[i] == listing[i+1]:
            return True
        
    return False


#main
k = []
emp = input("Please input a list of numbers separated by space: ").strip().split()
for component in emp:
    component = float(component)
    k.append(component)
print(two_length_run(k))
