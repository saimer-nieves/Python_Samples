
#Saimer nieves          Lab6B





#VAIRABLE DICTIONARY
#~Variables~
#response
#row_selection        user's selection for the row they'd like to sit in, returned from row_choice (known in function as row_r)
#seat_selection        user's selection for the seat they'd like to sit in, returned from seat_choice (known in function as seat_r)
#seat_returning             loop control variable, used for seat choice confirmation
#response             main loop control variable, used for user to reserve more than one seat
#confirm            used to control entering/exiting seat choice confirmation loop
#flag               flag variable used to determine if user selected an unreserved seat or not
#seat_sel           2-character string of where user has indivated they would like to reserve a seat
#~Lists~
#seatA_list              a list filled with seat A
#seatB_list              a list filled with seat B
#seatC_list              a list filled with seat C
#seatD_list              a list filled with seat D
#seats_selected     a list filled with all seats user has reserved during current session


from os import system, name 
  
#FUNCTIONS----------------------------------------

#A function that clears the console
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def another_seat():
    response=input("would you like to select another seat? ")
    return response

#a function that gathers the user's row choice and returns this value
def row_selection():

    row_returning = int(input("\t\t\tEnter the ROW you wish to sit in: "))
    
    #checks for valid row choice
    while row_returning < 1 or row_returning > 7: 
        row_returning = int(input("\t\t\tEnter the ROW you wish to sit in [1-7]: "))

    #return row_r value after validation; returns to wherever the call { row_choice() } exists in base program
    return row_returning

#a function that gathers the user's seat choice and returns this value
def seat_selection():

    seat_returning = input("\t\t\tEnter the SEAT you wish to sit in: ")
    seat_returning = seat_returning.upper() #uppercase equivalent of what has been entered

    #checks for valid seat choice
    while seat_returning != "A" and seat_returning != "B" and seat_returning != "C" and seat_returning != "D":
        seat_returning = input("\t\t\tEnter the SEAT you wish to sit in [A/B/C/D]: ")
        seat_returning = seat_returning.upper()

    #return seat_r value after validation; returns to wherever the call { seat_choice() } exists in base program
    return seat_returning


#a function that gathers the user's seat choice and returns this value
def seat_choice():

    seat_returning = input("\t\t\tEnter the SEAT you wish to sit in: ")
    seat_returning = seat_returning.upper() #uppercase equivalent of what has been entered

    #checks for valid seat choice
    while seat_returning != "A" and seat_returning != "B" and seat_returning != "C" and seat_returning != "D":
        seat_returning = input("\t\t\tEnter the SEAT you wish to sit in [A/B/C/D]: ")
        seat_returning = seat_returning.upper()

    #return seat_r value after validation; returns to wherever the call { seat_choice() } exists in base program
    return seat_returning


#BASE PROGRAM CODE--------------------------------------------------------------------------------------------------------


#initialize the seat lists
seatA_list = ['A','A','A','A','A','A','A']
seatB_list = ['B','B','B','B','B','B','B']
seatC_list = ['C','C','C','C','C','C','C']
seatD_list = ['D','D','D','D','D','D','D']

#i added this for final print to user of all seats reserved during the session
seats_taken = []

print("\t\t\t    AirDrogon ~ Valyria Bound Fight #4815")
print("\t\t\t -----------------------------------------")


response = input("\t\t\tEnter 'Y' to see the seating chart & begin selecting seats: ")
response = response.upper()
#while answer == "y":
while response == "Y" and response != "N":

    clear()
    #printing the seating chart
    print("\t\t\t    AirDrogon ~ Valyria Bound Fight #4815")
    print("\t\t\t -----------------------------------------")
    print("\t\t\t | \tROW # \t -   - \t\t -   - \t |")
    for i in range(0, 7):
        
        row = i + 1
        print("\t\t\t | \t", row, "\t", seatA_list[i], " ", seatB_list[i], "\t\t", seatC_list[i], " ", seatD_list[i], "\t |")

    print("\t\t\t ----------------------------------------- \n\n\n")

    row_req = row_selection() #return value has been validated in function

    seat_req = seat_selection() #return value has been validated in function

    #added confirmation to user; gives ability to change seat coice
    print("\n\t\t\tYou have requested the following seat:    {}. ".format(str(row_req) + seat_req))
    input("\t\t\tPress ENTER to continue")#used an inout() to pause the console

    #flag variable created; when flag color changes to red, error message that seat is taken appears
    flag = "green"

    #user can only select A or B or C or D, so elif statement used to filter to only one possible choice
    if seat_req == "A": #seatA list
        if seatA_list[row_req - 1] != "X": #seatA in this row has not been reserved yet
            
            #change seatA at row choice value to X for reserved
            seatA_list[row_req - 1] = "X"

            
        else:
            #this will only set flag to ref when the seatA at row choice is already reserved (seatA[row_req - 1] == "X")
            flag = "red"

    elif seat_req == "B": #seatB list

        if seatB_list[row_req - 1] != "X":
            seatB_list[row_req - 1] = "X"
            
        else:
            flag = "red"

    elif seat_req == "C": #seatC list

        if seatC_list[row_req - 1] != "X":
            seatC_list[row_req - 1] = "X"
            
        else:
            flag = "red"
    else: #seatD list
        if seatD_list[row_req - 1] != "X":
            seatD_list[row_req - 1] = "X"
            
        else:
            flag = "red"



    if flag == "red": #seat's taken
        print("\n\t\t\t\t**ERROR**") 
        print("\t\t\tSorry, seat's taken. Please choose another seat.")
        x = input("\t\t\tPress ENTER to continue to a new seat choice.") #input can be used to create a pause in console
    else:
        print()
    clear()

    #clear screen to reprint chart; this means the seating chart will stay in the same place

    print("\t\t\t    AirDrogon ~ Valyria Bound Fight #4815")
    print("\t\t\t -----------------------------------------")
    print("\t\t\t | \tROW # \t -   - \t\t -   - \t |")
    for i in range(0, 7):
        
        row = i + 1
        print("\t\t\t | \t", row, "\t", seatA_list[i], " ", seatB_list[i], "\t\t", seatC_list[i], " ", seatD_list[i], "\t |")

    print("\t\t\t ----------------------------------------- \n\n\n")

    response=input("would you like to select another seat? ")

    clear()


#--------------------------------------
#printing the seating chart for final reservation review
print("\t\t\t    AirDrogon ~ Valyria Bound Fight #4815")
print("\t\t\t -----------------------------------------")
print("\t\t\t | \tROW # \t -   - \t\t -   - \t |")
for i in range(0, 7):
        
    row = i + 1
    print("\t\t\t | \t", row, "\t", seatA_list[i], " ", seatB_list[i], "\t\t", seatC_list[i], " ", seatD_list[i], "\t |")

print("\t\t\t ----------------------------------------- \n\n\n")




print("\n\n\n\t\t\tThank you for choosing AirDrogon. Enjoy your trip to Valyria!\n\n\n\n\n")