import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    
    raw_file = None

    while raw_file == None:
        try:
            raw_file = input("Enter the name of the file: ").strip()
            f = open(raw_file)
            
            
        except FileNotFoundError:
            print("I can't find the file. Try again.")
            raw_file = None
    return f

def make_dict(lsw):
    read_fildi = {}
    for i in range(len(lsw)):
        for s in lsw[i]:
            if s in read_fildi:
                read_fildi[s].add(i+1)
            else:
                read_fildi.update({s:{i+1}})
    return read_fildi

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    read_filli = []
    all_inone = []
    lines = fp.read().splitlines()
    for line in lines:
        word = line.split()
        read_filli.append(word)
        
    for i in read_filli:
        tmp = []
        for k in i:
            if len(k) >= 2:
                tmp.append(rem_pun_for_main(k.lower()))
        all_inone.append(tmp)

    final_read_file=make_dict(all_inone)
    
    return final_read_file
    

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    coelines = []
    rest_ofline = {}
    
    coe = query.split()
    
    for i in range(len(coe)):
        coeline = D[coe[i]]
        coelines.append(coeline)
    
    rest_intersect = coelines[0]
    for p in coelines[1:]:
        rest_intersect = set(rest_intersect) & p

    mm = sorted(list(set(rest_intersect)))
    return mm

def is_valid(D,query,file):
    d = read_file(file)
    x = []
    not_in = ''
    x = query.split()
    for i in x:
        if i not in D:
            return i
    return not_in


def rem_pun_for_main(formain):
    formainn = ''
    if formain.isalpha() == True:
        return formain
    for k in range(len(formain)):
        if formain[k] not in string.punctuation:
            formainn += str(formain[k])
    return formainn
    
    
   
##############################
# main
##############################
file=open_file()
d=read_file(file)
querys=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE
query = rem_pun_for_main(querys)

while query != 'q':
    list_to_st = ''
    if len(query) == 0:
        print("Word '' not in the file.")
    else:
        flag = is_valid(d, query, file)

        if len(flag) == 0:
            coex_result = find_coexistance(d, query)
            if len(coex_result) == 0:
                print("The one or more words you entered does not coexist in a same line of the file.")
            else:
                for i in coex_result:
                    list_to_st = list_to_st + str(i) + " "
                print("The one or more words you entered coexisted in the following lines of the file:\n" + str(list_to_st))

        else:
            print("Word '" + flag + "' not in the file.")
    
    querys = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    query = rem_pun_for_main(querys)


