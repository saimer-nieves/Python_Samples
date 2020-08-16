
#Saimer Nieves Final Exam Practical

#Variable Dictionary=======================

#firstname              first name of student being search
#test1                  first test result of student
#test2                  second Test result of student
#test3                  third test result of student
#test4                  fourth test result of student
#test5                  fifth test result of student
#average                average test result list
#total_average          total average per student
#class_average          class average of all averages combined
#again{}                function the repeats another search
#goodbye()              goodbye functin ending program



#Defining Empty Variables====================



#Defining Functions ===========================


def goodbye():

    print("Thank you for using our Program. Come back soon")

def again():
    another = input("Would you like to search a Name again ? [y/n] ")

    while another != "y" and another != "Y" and another != "N" and another != "n":

        print("*ERROR*ERROR*")
        another = input("Would you like to search a Name again ? [y/n] ")


    #this function should return the user's selection AFTER checking that it is a valid input()
    return another
   


def swap(listname, position):
    t = listname[position]
    listname[position] = listname[position + 1]
    listname[position + 1] = t


# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep 
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


#This program builds and calls a clear screen function named clear.  Lines 4 - 18 

num_rec=0

firstName=[]
test1=[]
test2=[]
test3=[]
test4=[]
test5=[]

#import the library

import csv

with open("G:/final1.txt") as csvfile:
    #allow file data to be accessed as 'file'
    file = csv.reader(csvfile)

    
    #process file data using 'rec' and 'file'
    for rec in file:
        num_rec+=1
        firstName.append(rec[0])
        test1.append(int(rec[1]))
        test2.append(int(rec[2]))
        test3.append(int(rec[3]))
        test4.append(int(rec[4]))
        test5.append(int(rec[5]))
    

#"FILE CLOSED"----------------------------------------------------------------

#PROCESS LISTS = FOR LOOP!
average=[]
#Process the lists to reprint the file data, record by record
print("\t\t  Name: \t \tTest1: \t Test2:   Test3:    Test4:   Test5:\t \t Average:")
print("\n")

for index in range(0, num_rec):

    
    test_average = (test1[index] + test2[index] + test3[index] + test4[index] + test5[index]) / 5

    
    average.append(test_average)

class_average= 0
for index in range(0, num_rec):
    
    class_average+=average[index]

    total_average = (class_average / num_rec)



for index in range(0, num_rec):
    #REMEMBER: index = position in the list
    print(" INDEX:{0}\t {1:10}\t {2:10} \t{3:5}\t {4:5}\t {5:5}\t  {6:5}\t \t\t {7:5.2f}".format(index, firstName[index], test1[index], test2[index], test3[index], test4[index],test5[index], average[index]))
print("\n")
print("Total Number of Students Processed: ",num_rec)
print("Class Average: {0:5.2f}".format(total_average))
print("\n")





another = "y"


found= -1






while another == "y" or another == "Y" and another != "N" and another != "n":

        #4b - binary search will be performed w/ output to visualize search
        #BINARY SEARCH CAN ONLY BE USED ON ORDERED LISTS
        print("\nName Search: \n")
        #ask for search query
        
        search = input("Enter the Name you are looking for: ")

        #sort list & linked data --- FIRSTNAME, INCREASING
        for i in range(0, num_rec - 1):

            for k in range(0, num_rec - 1):

                if firstName[k] > firstName[k + 1]:#FIRSTNAME, INCREASING

                    #SWAP!
                    swap(firstName, k)
                    swap(test1, k)
                    swap(test2, k)
                    swap(test3, k)
                    swap(test4, k)
                    swap(test5, k)
                 

        #binary search list
        min = 0
        max = num_rec - 1
        guess = int((min + max) / 2) #cast as an integer to TRUNCATE -- remove decimal value

        while min < max and search != firstName[guess]:

            if search < firstName[guess]: #drop the "higher" half of the list

                max = guess - 1

            else: #search > firstName[guess], drop the "lower" half of the list

                min = guess + 1

            guess = int((min + max) / 2)

        #print results
        if search == firstName[guess]: #FOUND IT!
            index = index-1
            print("Your search for ", search, " was FOUND! Here's their info: ")
            print("\n")
            print("Name\tTest1\tTest2\tTest3\tTest4\tTest5\tAverage")
            personal_average = (test1[guess] + test2[guess] + test3[guess] + test4[guess] + test5[guess]) / 5
            print("{0:5}\t{1:5}\t{2:5}\t{3:5}\t{4:5}\t {5:5}    {6:5.2f}".format( firstName[guess], test1[guess], test2[guess], test3[guess], test4[guess],test5[guess], personal_average))
            print("\n")
        else: #not found :[
            
            print("This Search Was Not found----Try Again")
        
        another = again()
        



goodbye()