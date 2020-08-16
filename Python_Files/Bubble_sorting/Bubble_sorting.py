
#Saimer nieves LAB 7


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


#import the library

import csv

#initiate lists

num_rec = 0

#create empty lists in order to store file data -- one list per field in a file
idCode = []
lastName = []
firstName = []
age = []
allegiance = []




#funtions

#FUNCITONS-----------------------------------------------------------------------
def hello():

    print("Welcome to the SE126 FINAL REVIEW!")

def goodbye():

    print("Thank you for using our Program. When you play the game of thrones, you win or you die. Cersei Lannister")



def swap(listname, position):
    t = listname[position]
    listname[position] = listname[position + 1]
    listname[position + 1] = t


#menu funtion
def search_menu():

    print("1. Firstname")
    print("2. ID Code")
    print("3. Last NAme")
    print("4. Allegienace")
    print("5. Exit")

    response = int(input("Please enter your choice Number 1-5: "))

    while response != 1 and response != 2 and response != 3 and response != 4 and response != 5:

        print("*ERROR*ERROR*")
        response = int(input("Please enter your choice Number 1 -5 : "))


    #this function should return the user's selection AFTER checking that it is a valid input()
    return response






#import the file required

with open("C:/Users/Saimer/OneDrive/Desktop/Python_Files/Bubble_sorting/bubble_sort.txt") as csvfile:

    file = csv.reader(csvfile)

    #when reading files, each record is treated as a list
    #each field of data (rec[#]) represents a new value
    for rec in file:

        #this for loop will run for as many records (rows) of data in the file

        #store data into lists --> .append()
        idCode.append(rec[0])
        lastName.append(rec[1])
        firstName.append(rec[2])
        age.append(int(rec[3])) #casting as int for easier math processing
        allegiance.append(rec[4])
     

        num_rec += 1 


print("ID Code\t\tLast Name\tFirst Name\tAge\tAllegiance")
print("\n")
for i in range(0, num_rec):

    print("{0:10}\t{1:10}\t{2:10}\t{3:3}\t{4:32}".format(idCode[i], lastName[i], firstName[i], age[i], allegiance[i]))


print("\n")



answer="y"


while answer == "y" or answer =="Y" or answer =="N" or answer =="n":

    userChoice = search_menu()
#sequential Search   Last name and allegiance


    if userChoice == 3:
        
        print("\Last Name Search: \n")
        #ask for search query

        search = input("Enter the Last Name you are looking for: ")

        #run sequential search
        found = -1
        
        for i in range(0, num_rec):

            if search == lastName[i]:

               
                found = i
                
        #print results
      
                if found >= 0: 
            
                    
                    print("{0:10}\t{1:10}\t{2:10}\t{3:3}\t{4:32}\t".format(idCode[found], lastName[found], firstName[found], age[found], allegiance[found]))
                else: #not found :[

                    print("Error Try again")
   
    print("\n")
    if userChoice == 4:
        #4a - sequential search will be performed w/ output to visualize search
        print("\nAllegiance Search:\n")
        #ask for search query

        search = input("Enter the Allegiance you are looking for: ")

        #run sequential search
        found = -1
        
        for i in range(0, num_rec):

            if search == allegiance[i]:

               
                found = i
                
        #print results
      
                if found >= 0: 
            
                    
                    print("{0:10}\t{1:10}\t{2:10}\t{3:3}\t{4:32}\t".format(idCode[found], lastName[found], firstName[found], age[found], allegiance[found]))

                else: #not found :[

                    print("Error Try again")
    print("\n")

#Binary search  #First name and ID code


    if userChoice == 1:

        #4b - binary search will be performed w/ output to visualize search
        #BINARY SEARCH CAN ONLY BE USED ON ORDERED LISTS
        print("\nFirst Name Search: \n")
        #ask for search query

        search = input("Enter the FIRSTNAME you are looking for: ")

        #sort list & linked data --- FIRSTNAME, INCREASING
        for i in range(0, num_rec - 1):

            for k in range(0, num_rec - 1):

                if firstName[k] > firstName[k + 1]:#FIRSTNAME, INCREASING

                    #SWAP!
                    swap(firstName, k)
                    swap(idCode, k)
                    swap(lastName, k)
                    swap(age, k)
                    swap(allegiance, k)
                 

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
            
            print("Your search for ", search, " was FOUND! Here's their info: ")
            print("\n")
            print("{0:10}\t{1:10}\t{2:10}\t{3:3}\t{4:32}\t".format(idCode[guess], lastName[guess], firstName[guess], age[guess], allegiance[guess]))
            print("\n")
        else: #not found :[

            print("Error Try again")

    if userChoice == 2:

        #4b - binary search will be performed w/ output to visualize search
        #BINARY SEARCH CAN ONLY BE USED ON ORDERED LISTS
        print("\nID Code Search!\n")
        #ask for search query

        search = input("Enter the ID Code you are looking for: ")

        #sort list & linked data --- FIRSTNAME, INCREASING
        for i in range(0, num_rec - 1):

            for k in range(0, num_rec - 1):

                if idCode[k] > idCode[k + 1]:#FIRSTNAME, INCREASING

                    #SWAP!
                    swap(firstName, k)
                    swap(idCode, k)
                    swap(lastName, k)
                    swap(age, k)
                    swap(allegiance, k)
               

        #binary search list
        min = 0
        max = num_rec - 1
        guess = int((min + max) / 2) #cast as an integer to TRUNCATE -- remove decimal value

        while min < max and search != idCode[guess]:

            if search < idCode[guess]: #drop the "higher" half of the list

                max = guess - 1

            else: #search > firstName[guess], drop the "lower" half of the list

                min = guess + 1

            guess = int((min + max) / 2)

        #print results
        if search == idCode[guess]: #FOUND IT!
            
            print("Your search for ", search, " was FOUND! Here's their info: ")
            print("\n")
            print("{0:10}\t{1:10}\t{2:10}\t{3:3}\t{4:32}\t".format(idCode[guess], lastName[guess], firstName[guess], age[guess], allegiance[guess]))
            print("\n")
        else: #not found :[

            print("Error Try again")




    if userChoice == 5: 
            clear()
            print("\n Closing Program \n")
            #EXIT PROGRAM
            answer = "X"
            print("\n")
            goodbye()
            
            

        


