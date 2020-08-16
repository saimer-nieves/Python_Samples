

#WEEK 4 DAY 1: LIST PRACTICE & REVIEW DEMO

#PROMPT: Write a program that reads the data file (below) and stores the data into lists.  then, process the lists to reprint the file data, record by record. Next, reprocess the lists to find each student's current average score along with the class average.  Store each student's average into a new list called 'avg' and reprint the records to include the average.  Reprocess the lists one more time to find the letter equivalent of the average and store this into a new list called 'let_avg'.  Reprint the lists for a third and final time, record by record including average score and average letter equivalent.  After this third print, print to the console the total number of student's in the class along with the class numeric average.  



#NOTES: 
#       *All averages should be rounded to the 2nd decimal place.
#       *Process List = for loop
#       * 'index' represents location within a list when processing through a for loop 
#       * average = sum_total / num_items
#       * 90 >= A ; 90 < B >= 80; 80 < C >= 70; 70 < D >= 60; 60 < F
#       * FILE SETUP:
#           FIELD0      FIELD1      FIELD2      FIELD3      FIELD4
#           FIRSTNAME   LASTNAME    TEST1       TEST2       TEST3
#       *once all processing of lists has taken place, the following should appear for each student
#           FIRSTNAME   LASTNAME    TEST1       TEST2       TEST3       NUM AVG     LETTER AVG


#VARIABLE DICTIONARY----------------------

#records        total records within the file, also total number of values in each list
#csvfile        shorthand name for file location, full file path
#file           firendly name for file data, after it has been passed through csv.reader()
#rec            LIST, an inidivudal record from the file; only used when connected to file
#first          LIST, first names of students ( rec[0] )
#last           LIST, last names of students ( rec[1] )
#test1          LIST, test 1 scores of students ( rec[2] )
#test2          LIST, test 2 scores of students ( rec[3] )
#test3          LIST, test 3 scores of students ( rec[4] )
#average        average sudents test score; average = (test1 + test2 + test3) / 3
#avg            LIST, numeric averages of each student
#letter         letter equivalent of student's average, requires an if/elif/elif/elif/else chain
#avg_let        LIST, letter averages of each student
#class_total    sum total of all numeric averages in the class
#class_average  class numeric average; class_average = class_total / records



#BASE PROGRAM CODE------------------------------------------------------------------------------------------------------------

#import library for text file handling
import csv

#initialize variables for program (that will add to themselves)
records = 0

class_total = 0


#initialize empty lists for program - one list for every field in the text file
first_name = []
last_name = []
age = []
nickname = []
house_All = []

house_motto = []

#CONNECTED TO FILE-----------------------------------------------------------
#connect to file location any type of file can be inserted here with list information
with open("C:/Users/Saimer/OneDrive/Desktop/Python_Files/Python_Lists_4/List_Links.txt") as csvfile: 


    file=csv.reader(csvfile)

    for rec in file:
        #region to import data from file into the list

 




        records = records + 1
        first_name.append(rec[0])
        last_name.append(rec[1])
        age.append(rec[2])
        nickname.append(rec[3])
        house_All.append(rec[4])

     




    




for index in range(0, records):
    
    if house_All[index] == "House Stark":
       motto=  "Winter is Coming"
        
       
    
    elif house_All[index] == "House Baratheon":
       motto=  "Ours is the fury"
        
       
    elif house_All[index]  == "House Tully":
       motto=  "Family. Duty. Honor"
        
      
    elif house_All[index]== "Night's Watch":
       motto=  "And now my watch begins."
        
       

    elif house_All[index] == "House Targaryen":
       motto=  "Fire & Blood"
        
       

    elif house_All[index] == "House Lannister":
       motto=  "Hear me roar!"
        
      
   

    else:
       motto=  " Unknown Motto"
        
   
    house_motto.append(motto)

       #print entire student record including avg
    print("{0:10} {1:15} {2:5} {3:20} {4:20}     {5:20}".format(first_name[index], last_name[index], age[index], nickname[index], house_All[index], house_motto[index]))

  


 
 
    


    


