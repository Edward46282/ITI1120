import math
import random

def elementary_school_quiz(flag, n):
    '''
    (int, int) -> int
    Preconditions: flag is 0 or 1, n is 1 or 2
    This quiz is for elementary school as it only tests subtraction and exponention.
    '''
    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    num_of_correct = 0
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    num3 = random.randint(1, 9)
    num4 = random.randint(1, 9)
    if flag == 0 and n == 1:
        t1 = input("Question 1:\nWhat is the result of " + str(num1) + "-" + str(num2) + "?\t")
        ans1 = num1-num2
        if ans1 == int(t1):
            return 1
        else:
            return 0
        
    elif flag == 0 and n == 2:
        t2 = input("Question 1:\nWhat is the result of " + str(num1) + "-" + str(num2) + "?\t")
        ans2 = num1 - num2
        if ans2 == int(t2):
            num_of_correct += 1
        t3= input("Question 2:\nWhat is the result of " + str(num3) + "-" + str(num4) + "?\t")
        ans3 = num3 - num4
        if ans3 == int(t3):
            num_of_correct += 1
        return num_of_correct

    elif flag == 1 and n ==1:
        e1 = input("Question 1:\nWhat is the result of " + str(num1) + "^" + str(num2) + "?\t")
        ansp = pow(num1, num2)
        if ansp == int(e1):
            return 1
        else:
            return 0

    elif flag == 1 and n == 2:
        e2 = input("Question 1:\nWhat is the result of " + str(num1) + "^" + str(num2) + "?\t")
        ansp = pow(num1, num2)
        if ansp == int(e2):
            num_of_correct += 1
        e3 = input("Question 2:\nWhat is the result of " + str(num3) + "^" + str(num4) + "?\t")
        ansp2 = pow(num3, num4)
        if ansp2 == int(e3):
            num_of_correct += 1
        return num_of_correct
        
    # Your code should include  dosctrings and the body of the function
    #
    #


def high_school_quiz(a,b,c):
    '''
    (num, num, num) -> none
    if the user gives three values, the function prints an equation using the values. And then, it prints the root/roots
    '''
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    if a != 0 and b != 0 and c!= 0:
        print("The quadratic equation " + str(a) + "·x^2 + " + str(b) + "·x + " + str(c) + " = 0")
        if (b**2 - 4 * a * c) > 0:
            x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
            x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
            print ("has the following real roots:\n" + str(x1) + " and " + str(x2))
        elif (b**2 - 4 * a * c) == 0:
            x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
            print ("has only one solution, real root:\n" + str(x1))
        elif (b**2 - 4 * a * c) < 0:
            num_im = (-b)/(2*a)
            im_included = " i " + str(math.sqrt(abs(b**2 - 4 * a * c))/ (2*a))
            x1 = str(num_im) + " + " + im_included
            x2 = str(num_im) + " - " + im_included
            print ("has the following two complex roots:\n" + str(x1) + " \nand\n" + str(x2) )

    elif a == 0 and b != 0 and c!= 0:
        print("The linear equation " + str(b) + "·x + " + str(c) + " = 0")
        sol_noa = -c/b
        print("has the following root/solution: " + str(sol_noa))

    elif a == 0 and b == 0 and c == 0:
        print("The quadratic equation 0·x + 0 = 0\nis satisifed for all number x")

    elif a == 0 and b == 0 and c != 0:
        print("The quadratic equation 0·x + " + str(c) + " = 0\nis satisified for no number x")



# main

# your code for the welcome tmessage goes here
print("*******************************************")
print("*                                         *")
print("*  __Welcome to my math quiz-generator__  *")
print("*                                         *")
print("*******************************************")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':
    width_of_border = len(name)+70
    print("*" * width_of_border)
    print("*" + " " * (width_of_border -2) + "*")                                                    
    print("* __"+name+", welcome to my quiz-generator for elementary school students.__ *")
    print("*" + " " * (width_of_border -2) + "*") 
    print("*" * width_of_border)
    flag = int(input(name + " what would you like to practice? Enter\n0 for subtraction\n1 for exponentiation\n"))
    if flag != 0 and flag != 1:
        print ("Invalid choice. Only 0 or 1 is accepted")
    else:
        n = int(input("How many practice questions would you like to do? Enter 0, 1, or 2:\t"))
        if n == 0:
            print("Zero questions. OK. Good bye")
        elif n > 2:
            print("Only 0,1, or 2 are valid choices for the number of questions.")
        else:
            print(name + ", here is your " + str(n) +" questions:\n")
            result = (elementary_school_quiz(flag,n))
            if int(result)/ int(n) == 1:
                print("Congratulations " + name + "! You’ll probably get an A tomorrow.")

            elif int(result)/ int(n) == 0.5:
                print("You did ok " + name + ", but I know you can do better.")

            else:
                print("I think you need some more practice " + name +".")

elif status=='2':

    width_of_border = len(name) + 60
    print("*" * width_of_border)
    print("*" + " " * (width_of_border -2) + "*")                                                                      
    print("  __quadratic equation, a·x^2 + b·x + c= 0, solver for "+ name +"__  *")
    print("*" + " " * (width_of_border -2) + "*")
    print("*" * width_of_border)

    # your code for welcome message
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here
        question = question.lower()
        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
            a= float(input("Enter a number the coefficient a: "))
            b= float(input("Enter a number the coefficient b: "))
            c= float(input("Enter a number the coefficient c: "))
            high_school_quiz(a,b,c)
 
else:
    print(name + " you are not a target audience for this software.")

print("Good bye "+name+"!")
