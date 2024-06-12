def number_divisible(li,di):
    '''
    (list of ints, int) -> int
    This function takes a list of integers and a integer n as input parameters and returns the number of elements in the list that are divisible by n.
    '''
    coun = 0
    for i in li:
        if i % di == 0:
            coun += 1
    return coun


#main
user_input = input("Please input a list of numbers seperated by space: ").strip().split()
for i in range(len(user_input)):
    user_input[i] = int(user_input[i])
seco_input = input("Please input an integer: ").strip()
final = number_divisible(user_input,int(seco_input))
print("The number of elements divisible by " + seco_input + " is " + str(final))
