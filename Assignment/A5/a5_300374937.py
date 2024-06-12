import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]

    # YOUR CODE GOES HERE
    new_list = []
    sublist = []
    for i in friends:
        x = i.split(" ")
        new_list.append(x)

    
    for k in range(1,len(new_list)):
        flag = False
        first = int(new_list[k][0])
        second = int(new_list[k][1])
        third_flag = False
        for s in range(len(sublist)):
            second_flag = False
            if first == sublist[s][0]:
                sublist[s][1].append(second)
                for t in range(len(sublist)):
                    if second == sublist[t][0]:
                        sublist[t][1].append(first)
                        second_flag = True
                if second_flag == False:
                    sublist.append([second,[first]])
                flag = True
                  
        if flag == False:
            sublist.append([first,[second]])
            for fin in range(len(sublist)):
                if second == sublist[fin][0]:
                    sublist[fin][1].append(first)
                    third_flag = True
            if third_flag == False:
                sublist.append([second,[first]])

    sublist.sort()

    for matu in sublist:
        matu = tuple(matu)
        network.append(matu)
    
    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    
    # YOUR CODE GOES HERE
    us1 = []
    us2 = []
    for i in network:
        if user1 == i[0]:
            us1.append(i[1])
        elif user2 == i[0]:
            us2.append(i[1])

    us1 = us1[0]
    us2 = us2[0]

    for com in range(len(us1)):
        for co in range(len(us2)):
            if us1[com] == us2[co]:
                common.append(us1[com])

    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE
    friends = []
    ffriend = []
    newlist = []
    final_ans = 0
    for i in network:
        if i[0] == user:
            friends = i[1]
            
    for s in friends:
        for k in network:
            if s == k[0]:
                ffriend.append(k[1])
    
    friends.append(user)
    for frien in ffriend:
        for j in range(len(frien)):
            if frien[j] not in friends:
                newlist.append(frien[j])
    newlist.sort()
    
    if len(newlist) == 1:
        return newlist[0]
    elif len(newlist) == 0:
        return None
    counter = 0
    counting = []
    for i in range(len(newlist)-1):
        if newlist[i] == newlist[i+1]:
            counter += 1
        else:
            counting.append([counter, newlist[i]])
            counter = 0
        if i == len(newlist)-2:
            counting.append([counter, newlist[i]])
    counting.sort()
    counting = counting[::-1]
    
    final_ans = counting[0][1]
    return final_ans


    

def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    counting4 = 0
    for i in network:
        if len(i[1]) >= k:
            counting4 += 1
    return counting4

 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    maxi_numfr = 0
    for i in network:
        if len(i[1]) > maxi_numfr:
            maxi_numfr = len(i[1])
    return maxi_numfr

    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE -> mark the index of the most friends
    len_of_friends = 0
    for i in range(len(network)):
        if len(network[i][1]) > len_of_friends:
            len_of_friends = len(network[i][1])

    for j in network:
        if len(j[1]) == len_of_friends:
            max_friends.append(j[0])
    return    max_friends



def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
    averagins = 0
    for i in network:
        averagins += len(i[1])

    averagins = averagins/len(network)

    return averagins

    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE
    for i in network:
        if len(i[1]) == len(network)-1:
            return True
    return False



####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE
    list_of_friendsfirst = []
    for i in network:
        list_of_friendsfirst.append(str(i[0]))


    raw_input_fromtheuser_get = input("Enter an integer for a user ID: ").strip().lower()
    checking_dig = raw_input_fromtheuser_get.isdigit()
    for i in raw_input_fromtheuser_get:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            contains_alpha = True
        
    
    if contains_alpha != True and int(raw_input_fromtheuser_get) < 0 and raw_input_fromtheuser_get[1:].isdigit() == True:
        checking_dig = True
    while checking_dig == False:
        contains_alpha = False
        print("That was not an integer. Please try again.")
        raw_input_fromtheuser_get = input("Enter an integer for a user ID: ").strip().lower()
        for i in raw_input_fromtheuser_get:
            if i in 'abcdefghijklmnopqrstuvwxyz':
                contains_alpha = True
            
        checking_dig = raw_input_fromtheuser_get.isdigit()
      
        
        if contains_alpha != True and int(raw_input_fromtheuser_get) < 0 and raw_input_fromtheuser_get[1:].isdigit() == True:
            checking_dig = True
        
        if checking_dig == True and raw_input_fromtheuser_get not in list_of_friendsfirst:
            while checking_dig == True and raw_input_fromtheuser_get not in list_of_friendsfirst:
                print("That user ID does not exist. Try again.")
                raw_input_fromtheuser_get = input("Enter an integer for a user ID: ").strip()
                checking_dig = raw_input_fromtheuser_get.isdigit()
    if checking_dig == True and raw_input_fromtheuser_get in list_of_friendsfirst:
        return int(raw_input_fromtheuser_get)
        

    

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
