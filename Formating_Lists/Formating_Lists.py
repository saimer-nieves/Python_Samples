
#Saimer Nieves 2-5-2020              MIdterm Pratical


#import library for text file handling
import csv

#initialize variables for program (that will add to themselves)
records = 0

class_total = 0

average=0
#initialize empty lists for program - one list for every field in the text file
player_name = []
character_name = []
level = []
race = []
class_type = []

hit_points=[]
avg=[]
#CONNECTED TO FILE-----------------------------------------------------------
#connect to file location
with open("G:/SE126 MIDTERM FILES/campaign1.txt") as csvfile:


    file=csv.reader(csvfile)

    for rec in file:
        #region to import data from file into the list

    #Field Change location

        field0=rec[0]       
        field1=rec[1]
        field2=rec[2]
        field3=rec[3]
        field4=rec[4]


    #Store into proper lists

        records = records + 1


        player_name.append(field0)
        character_name.append(field1)
        level.append(field2)
        race.append(field3)
        class_type.append(field4)

     




    

print(" \t \t  Player Name:    Character Name:      Level: \t Race:   \t Class Type:  ")
print("\n")

for index in range(0, records):
    
    

       #print entire student record including avg

   
    print("\t\t    {0:10} \t\t {1:15} {2:5}   {3:11} \t {4:20}     ".format(player_name[index], character_name[index], level[index], race[index], class_type[index]))
print("\n")
print("Total Number of Players in File:", records)

print("\n")
print("\n")
print("\n")


def hit_sum():
    hit_points.append(hits)
    average+= int(hits)
    avg.append(hits)


print(" \t \t  Player Name:    Character Name:      Level: \t Race:   \t Class Type:  \t Hit Points: ")

print("\n")
for index in range(0, records):
    
    if class_type[index] == "Barbarian":
       hits=  "45"
        
       
    
    elif class_type[index] == "Bard":
       hits=  "33"
        
       
    elif class_type[index]  == "Cleric":
       hits=  "38"
        
      
    elif class_type[index]== "Druid":
       hits=  "32"
        
       

    elif class_type[index] == "Fighter":
       hits=  "40"
        
       

    elif class_type[index] == "Monk":
       hits=  "34"

    elif class_type[index] == "Paladin":
       hits=  "39"

    elif class_type[index] == "Ranger":
       hits=  "37"

    elif class_type[index] == "Rogue":
       hits=  "31"

    elif class_type[index] == "Sorcerer":
       hits=  "27"

    elif class_type[index] == "Warlock":
       hits=  "30"

    elif class_type[index] == "Wizard":
       hits=  "28"
        
      
   

    else:
       hits=  " Unknown Hit Points"
        
   
    hit_points.append(hits)
    average+= int(hits)
    avg.append(hits)

       #print entire student record including avg
    print("\t\t    {0:10} \t\t {1:15} {2:5}   {3:11} \t {4:20}  \t {5:5}   ".format(player_name[index], character_name[index], level[index], race[index], class_type[index], hit_points[index]))

print("\n")
print("Average Base hits:  {0:5.1f}".format(int(avg[index])))


print("Total Number of Players in File:", records)