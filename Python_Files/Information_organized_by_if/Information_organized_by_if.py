
#Saimer Nieves       Lab 5B 

#Dictionary ========================================


#id_number             Persons ID number
#age                    persons age number
#not_old                number count of people not old enough to register
#gender                 persons gender
#male_count             count number of people that are male
#yes_old                  #number count of adults
#female_count             #female number count
#yes_register             #number count of indidviduals who have registered
#no_register              #number count of individuas who have not registered
#yes_voted                #number count of people who voted 
#no_voted                 #number count of peple who
#records_proccessed       #number of records proccessed
#register                 #number of people registered
#young_males             #number of males underage
#young_women               #number of females underage
#YMnot_resgistered        #number of adult males not registered

#YWnot_registered          #number of adult females not registered
#elig_notvoted             #number of people who are adults, registered, but not voted









#Defined Variables ---------------------------------------------------


not_old = 0                 #number count of underage individuals
yes_old = 0                 #number count of adults

male_count = 0              #male number count
female_count = 0            #female number count
yes_register = 0            #number count of indidviduals who have registered
no_register = 0             #number count of individuas who have not registered
yes_voted = 0               #number count of people who voted   
no_voted = 0                #number count of peple who
records_proccessed = 0      #number of records proccessed
register = 0                #number of people registered
young_males = 0             #number of males underage
young_women=0               #number of females underage
YMnot_resgistered=0         #number of adult males not registered
YWnot_registered=0          #number of adult females not registered
elig_notvoted=0             #number of people who are adults, registered, but not voted


#Key to entrance for while loop----------------------------------------------------------------------------------------


another = input("PRESS ""Y"" TO BEGIN:  ")


#while loop gate--------------------------------------------------------------------------------------------------------

while another == "Y":
#input
    id_number = int(input("What is your ID Number? :"))                 #questioning for ID Number
    age = int(input("What is your age? : "))            #input for age 


#Updating IF statements for counters
#Minor counter
    if age < 18 :
        
        not_old = not_old + 1

#Adult counter
    if age >= 18:
        
        yes_old = yes_old + 1



#Input
    gender = input("what is your gender? (M/F)")        #Gender input data


#Updating Gender Counter with IF staments

#Male Counter Update
    if  gender == "M":
        male_count = male_count + 1

#Female Counter Update
    if gender == "F":
        female_count = female_count + 1 

 #Input 
    register = input("Are you register to vote? (Y/N):")    #Input data for people who have registered

#Updating Registered counter with IF statements

#People who have registered Counter
    if register == "Y" :
        yes_register = yes_register + 1 

#People who have not registered Counter
    if register == "N" : 
        no_register = no_register + 1
        

#Input
    voted = input("Have you voted? (Y/N) :")        #Input of people if they voted or not

#Updating voting counter 

#People who have voted 
    if voted == "Y":  
        yes_voted = yes_voted + 1
#people who have not voted
    if voted == "N":
        no_voted = no_voted + 1



#Updating the number of records proccessed as we approach end of loop
    records_proccessed = records_proccessed + 1

#Input
    another = input("enter another person? (Y/N) ")         #input data of asking if loop wants to be repeated to enter another person

    print("\n")     #space
    print("\n")     #space


    #COUNTER OF ALL UPDATING COUNTERS DISPLAY OUTPUT. THIS SHOWS UPDATES AFTER EVERY PROCESSED FILE
    print("Total People :  {0:.0f}      Male Count {1:.0f}    Female Count {2:.0f}       Registered:  {3:.0f}       Voted: {4:.0f}  ".format(records_proccessed, male_count, female_count, yes_register ,yes_voted))
  




   


#Formulas for combination of information
    if age < 18 and gender =="M":
        young_males = young_males + 1
    if age < 18 and gender == "F":
        young_women = young_women + 1
    if age >= 18 and gender =="M" and register == "N":
        YMnot_resgistered = YMnot_resgistered + 1
    if age >= 18 and gender =="F" and register == "N": 
        YWnot_registered = YWnot_registered + 1
    if age >= 18 and register == "Y" and voted == "N":

#Updating counter of people who are eligable but not voted

        elig_notvoted = elig_notvoted + 1

    print("____________________________________________")#Divider

print("\n")
print("\n")


#Output Display ---------------------------------------------
print ("Males not eligible to register:      ", young_males)
print("Females not eligible to register:     ", young_women)
print("Males who are old enough to vote but have not registered:      ",YMnot_resgistered)
print("Females who are old enough to vote but have not registered:    ", YWnot_registered,)
print("Individuals who are eligible to vote but did not vote:         ", elig_notvoted)
print("People who voted:      ", yes_voted )
print( "Records Proccessed:   ", records_proccessed,)


#Right answers according to KT!
#1
#1
#1
#1
#2
#6
#12



#2 age no
#10 age yes
#5 male count
#7 female count
#8 yes register
#4  no register
#6 yes voted
#6 no voted







