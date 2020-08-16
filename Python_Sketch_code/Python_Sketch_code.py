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


new_ID = 2029

print("\n")
print("\n")
print("\n")

print("                                                  GYM PROGRAM")
print("\n")
print("\n")
new_user = input("                                Welcome...are you  a new user?  ")
print("\n")
print("\n")
clear()
if new_user== "y" or new_user=="Y":
    new_ID = new_ID +1

    print("\n")
    print("\n")

    print("\n")

    print("                                                  GYM PROGRAM")
    print("\n")
    print("\n")

    print("                                 Create a Sign in:")
    print("\n")
    correct_username = input("                                        username:   ")
    print("\n")
    correct_password = input("                                        password:   ")
    print("\n")
    match_password = input("                                repeat password:    ")



#PASSWORD LOOP
    while match_password != correct_password :
            clear()
            print("\n")
            print("\n")
            print("\n")
            print("\n")

            print("                                   Passwords Did not match, please try again")
            print("\n")
            print("\n")
            correct_username = input("                                        username:   ")
            print("\n")
            correct_password = input("                                        password:   ")
            print("\n")
            match_password = input("                                repeat password:    ")

    previous_password = correct_password 
    previous_username = correct_username



#an old user
if new_user =="n" or new_user =="N":
    print("                                                 LOG IN")
    previos_username = input("                                        username:   ")
    print("\n")
    previous_password = input("                                        password:   ")
    print("\n")
   
    if previous_username == correct_username:
        print("correct Username")
    if previous_password == correct_password:
        print("correct_password")
    else:
        print("invalid ID Login")
    log_out = input("do you wish to log out")





clear()
print("\n")
print("\n")
print("                            WELCOME TO OUR GYM CALORIES BURNER PROGRAM")
print("\n")
sleep(2)

print("\n")
print("             Hello, ",correct_username,":")
print("\n")
print("                      Here we would like to help  you  burn  calories at the gym as you")
print("                      work out, but first we want get get more information about you")
print("\n")
sleep(6)
import time
import sys

done = 'false'
#here is the animation
def animate():
    if done == 'false':
        sys.stdout.write('\r                                .')
        time.sleep(1)
        sys.stdout.write('\r                                ..')
        time.sleep(0.8)
        sys.stdout.write('\r                                ...')
        time.sleep(0.7)
        sys.stdout.write('\r                                ....')
        time.sleep(0.7)

animate()

clear()

print("\n")
print("\n")



print ("                                       ",correct_username,"'s  WEIGHT LOST TRAINING")
print("\n")


current_weight = int(input("                  Current Weight (lbs):  "))
print("\n")
final_weight = int(input("                   Final Weight (lbs):   "))
print("\n")

days = int(input("                      How many days :    "))



clear()

weight_change = final_weight - current_weight


cal_pound = 3500

total_calories = cal_pound * weight_change

cal_perday = total_calories / days
print("\n")

print("                                                      EXERCISE MENU ")
print("\n")
print("                    {0:10}        {1:10}       {2:10}         {3:10}        {4:10}".format("Starting." ,"Ending",  "weight", "total", "calories"))   #headers
print("                    {0:10}      {1:10}         {2:10}        {3:10}         {4:10}".format(" Weight" ,"  Weight",  "Change", "calories", "Per day"))
print("\n")
print("                  {0:10.0f}\t {1:10,.0f} \t {2:10,.0f} \t      {3:10,.0f} \t {4:10,.0f} \t  ".format(current_weight, final_weight,  weight_change, total_calories, cal_perday))   


#Calculator option menu
print("\n")
print("                       =============================================================================")
print("\n")
print("                                                     EXERCISE MENU") 
print("\n")
print("                             {0:10}       {1:10}     {2:10}     ".format("High-Intensity. ","Med-Intensity." ,"Low-Intensity.")) 
print("\n")
print("                             {0:10}       {1:10}        {2:10}     ".format("(1) Mountain Climb","(5) Burpees" ,"(9) rowing")) 
print("                             {0:10}           {1:10}        {2:10}     ".format("(2) jump jacks","(6) Stairs " ,"(10) push-ups")) 
print("                             {0:10}            {1:10}      {2:10}     ".format("(3) jump-rope","(7) bicycling" ,"(11) squats")) 
print("                             {0:10}              {1:10}       {2:10}     ".format("(4) running","(8) jogging." ,"(12) walking")) 
print("\n")

expand = input("                                             press X to expand menu")

#GOTTA ADD DETAILS
if expand == "x" or expand == "X":
    clear()
    print("\n")
    print("                                                     EXERCISE MENU") 
    print("\n")

    print("                             {0:10}          {1:10}           {2:10}     ".format("High-Intensity. ","Med-Intensity." ,"Low-Intensity.")) 

    print("\n")

    print("\n")
    print("                             {0:10}        {1:10}               {2:10}     ".format("(1) Mountain Climb","(5) Burpees" ,"(9) rowing")) 
    print("                                 {0:10}           {1:10}              {2:10}     ".format("10.5 Cal/Min","12.5 Cal/Min" ,"7 cal/min")) 
     
    print("\n")
    print("                             {0:10}            {1:10}               {2:10}     ".format("(2) jump jacks","(6) Stairs " ,"(10) push-ups")) 
    print("                                  {0:10}          {1:10}            {2:10}     ".format("13 cal/min "," 10.5 cal/24 steps" ,"8 cal/min"))
    print("\n")
    print("                             {0:10}             {1:10}             {2:10}     ".format("(3) jump-rope","(7) bicycling" ,"(11) squats")) 
    print("                                 {0:10}           {1:10}               {2:10}     ".format("17 Cal/min "," 10 cal/min" ,"10.5 cal/min ")) 
 
    print("\n")
    print("                             {0:10}               {1:10}              {2:10}     ".format("(4) running","(8) jogging." ,"(12) walking")) 
    print("                                 {0:10}          {1:10}               {2:10}     ".format("15 Cal/Min ","10 cal / min " ,"5 Cal/min")) 
print("\n")

print("                                      Choose 3 Exercise for you to focus on ")
print("\n")
first_exercise = input("                                                      ")
mountain = 1

inputs = 0

while inputs <= 3:
    def menu():
        clear()
        print("\n")
        print("                                                     EXERCISE MENU") 
        print("\n")
        print("                             {0:10}        {1:10}               {2:10}     ".format("(1) Mountain Climb","(5) Burpees" ,"(9) rowing")) 
        print("                                 {0:10}           {1:10}              {2:10}     ".format("10.5 Cal/Min","12.5 Cal/Min" ,"7 cal/min")) 
     
        print("\n")
        print("                             {0:10}            {1:10}               {2:10}     ".format("(2) jump jacks","(6) Stairs " ,"(10) push-ups")) 
        print("                                  {0:10}          {1:10}            {2:10}     ".format("13 cal/min "," 10.5 cal/24 steps" ,"8 cal/min"))
        print("\n")
        print("                             {0:10}             {1:10}             {2:10}     ".format("(3) jump-rope","(7) bicycling" ,"(11) squats")) 
        print("                                 {0:10}           {1:10}               {2:10}     ".format("17 Cal/min "," 10 cal/min" ,"10.5 cal/min ")) 
    
        print("\n")
        print("                             {0:10}               {1:10}              {2:10}     ".format("(4) running","(8) jogging." ,"(12) walking")) 
        print("                                 {0:10}          {1:10}               {2:10}     ".format("15 Cal/Min ","10 cal / min " ,"5 Cal/min")) 
        print("\n")
        print("\n")
        print("                                      Choose 3 Exercise for you to focus on ")   #display of exercise menu
    print("\n")


    inputs = inputs + 1
    


    #dispplay of selected exercise

    if inputs == 1:
        menu()
        

        
        if first_exercise  == "1" :
            print("                                    1st - Mountain Climber")
            first = "Mountain Climber"
            first_totalcal = 10.5


        if first_exercise  == "2" :
            print("                                     1st - jumping Jacks")
            first = "Jumping Jacks"               
            first_totalcal = 13


        if first_exercise  == "3" :
            print("                                     1st - Jump rope")
            first = "Jump rope"
            first_totalcal = 17


        if first_exercise  == "4" :
            print("                                     1st - running")
            first = "running"
            first_totalcal = 15


        if first_exercise  == "5" :
            print("                                     1st - Burpess")
            first = "Burpess"
            first_totalcal = 12.5


        if first_exercise  == "6" :
            print("                                     1st - stairs")
            first = "stairs"
            first_totalcal = 10.5


        if first_exercise  == "7":
            print("                                     1st - bicycling")
            first = "bicycling"
            first_totalcal = 10


        if first_exercise  == "8" :
            print("                                     1st - jogging")
            first = "jogging"
            first_totalcal = 10


        if first_exercise  == "9" :
            print("                                     1st - rowing")
            first = "rowing"
            first_totalcal = 7


        if first_exercise  == "10" :
            print("                                     1st - push-ups")
            first = "push-ups"
            first_totalcal = 6


        if first_exercise  == "11" :
            print("                                     1st - squats")
            first = "squats"
            first_totalcal = 10.5


        if first_exercise  == "12" :
            print("                                     1st - walking")
            first = "walking"
            first_totalcal = 5
        

        second_exercise = input("                                                      ")
    if inputs == 2:
        menu()
        
        
        if  second_exercise == "1":
            print("                                    2nd - Mountain Climber")
            second = "Mountain Climber"
            second_totalcal = 10.5

        if  second_exercise == "2":
            print("                                    2nd - jumping Jacks")
            second = "jumping Jacks"
            second_totalcal = 13

        if second_exercise == "3":
            print("                                    2nd - Jump rope")
            second = "Jump rope"
            second_totalcal = 17

        if  second_exercise == "4":
            print("                                    2nd - running")
            second = "running"
            second_totalcal = 15
        if  second_exercise == "5":
            print("                                    2nd - Burpess")
            second = "Burpess"
            second_totalcal = 12.5

        if  second_exercise == "6":
            print("                                    2nd - stairs")
            second = "stairs"
            second_totalcal = 10.5

        if  second_exercise == "7":
            print("                                    2nd - bicycling")
            second = "bicycling"
            second_totalcal = 10

        if  second_exercise == "8":
            print("                                    2nd - jogging")
            second = "jogging"
            second_totalcal = 10

        if  second_exercise == "9":
            print("                                    2nd - rowing")
            second = "rowing"
            second_totalcal = 7

        if  second_exercise == "10":
            print("                                    2nd - push-ups")
            second = "push-ups"
            second_totalcal = 6

        if  second_exercise == "11":
            print("                                    2nd - squats")
            second = "squats"
            second_totalcal = 10.5

        if  second_exercise == "12":
            print("                                    2nd - walking")
            second = "Walking"
            second_totalcal = 5
        third_exercise = input("                                                      ")

    if inputs == 3:
        menu()
        
        
        if third_exercise  == "1":
            print("                                     3rd - Mountain Climber")
            third = "Mountain Climber"
            third_totalcal = 10.5

        elif third_exercise  == "2":
            print("                                    3rd - jumping Jacks")
            third = "jumping Jacks"
            third_totalcal = 13

        elif third_exercise  == "3":
            print("                                    3rd - Jump rope")
            third = "Jump rope"
            third_totalcal = 13

        elif third_exercise  == "4":
            print("                                    3rd - running")
            third = "running"
            third_totalcal = 15

        elif third_exercise  == "5":
            print("                                    3rd - Burpess")
            third = "Burpess"
            third_totalcal = 12.5

        elif third_exercise  == "6":
            print("                                    3rd - stairs")
            third = "stairs"
            third_totalcal = 10.5

        elif third_exercise  == "7":
            print("                                    3rd - bicycling")
            third = "bicycling"
            third_totalcal = 10

        elif third_exercise  == "8":
            print("                                    3rd - jogging")
            third = "jogging"
            third_totalcal = 10

        elif third_exercise  == "9":
            print("                                    3rd - rowing")
            third = "rowing"
            third_totalcal = 7

        elif third_exercise  == "10":
            print("                                    3rd - push-ups")
            third = "push-ups"
            first_totalcal = 6

        elif third_exercise  == "11":
            print("                                    3rd - squats")
            third = "squats"
            third_totalcal = 10.5

        elif third_exercise  == "12":
            print("                                    3rd - walking")
            third = "walking"
            third_totalcal = 5

print("\n")



exit = input("                                                          PRESS X TO CONTINUE")




clear()

print("\n")


#algarotithm

sets = 3 
reps = 20

sets_2nd = 3
reps_2nd = 15

sets_3rd = 4
reps_2nd = 10

each_exercisecal = cal_perday / 3

first_time_exercise = each_exercisecal / first_totalcal * -1
second_time_exercise = each_exercisecal / second_totalcal * -1
third_time_exercise = each_exercisecal / third_totalcal * -1



#Formulas for calories burned by exercise
calburn_one = first_totalcal * first_time_exercise
calburn_two =  second_totalcal * second_time_exercise
calburn_three =  third_totalcal * third_time_exercise
print("______________________________________________________________________________________________________________________________________________")

print("                                                                       Today's Workout")

print("\n")
print("\n")
print("                              {0:16}            {1:16}       {2:16}        {3:16}          {4:16}  ".format("Exercise." ,"sets", "Reps", "calories Burned", "time Mins"))   #headers
print("\n")
print("                         {0:16}   {1:16}       {2:16}            {3:16.0f}         {4:16.0f}  ".format(first, sets, reps, first_totalcal, first_time_exercise))  
sleep(0.5)
print("                         {0:16}   {1:16}       {2:16}            {3:16.0f}         {4:16.0f}  ".format(second, sets, reps, second_totalcal, second_time_exercise)) 
sleep(0.5)
print("                         {0:16}   {1:16}       {2:16}            {3:16.0f}         {4:16.0f}  ".format(third, sets, reps, third_totalcal, third_time_exercise )) 

finish_cal = cal_perday * -1
total_time = first_time_exercise + second_time_exercise + third_time_exercise
print("\n")
print("                                                                                           Workout                           Total")
print("                                                                                           Cal Burned:  {0:6.0f} Cal            Time:{1:5.0f} Mins".format(finish_cal , total_time ))

print("______________________________________________________________________________________________________________________________________________")

print("\n")
print("                                                                  Tomorrows Workout")
print("\n")
print("\n")
print("                              {0:16}            {1:16}       {2:16}        {3:16}          {4:16}  ".format("Exercise." ,"sets", "Reps", "calories Burned", "time Mins"))   #headers
print("\n")

print("\n")
print("                         {0:16}   {1:16}       {2:16}            {3:16.0f}         {4:16.0f}  ".format(third, sets, reps, third_totalcal, third_time_exercise )) 
sleep(0.5)
print("                         {0:16}   {1:16}       {2:16}            {3:16.0f}         {4:16.0f}  ".format(second, sets, reps, second_totalcal, second_time_exercise)) 
sleep(0.5)
print("                         {0:16}   {1:16}       {2:16}            {3:16.0f}         {4:16.0f}  ".format(first, sets, reps, first_totalcal, first_time_exercise)) 


finish_cal = cal_perday * -1
total_time = first_time_exercise + second_time_exercise + third_time_exercise
print("\n")
print("                                                                                           Workout                           Total")
print("                                                                                           Cal Burned:  {0:6.0f} Cal            Time:{1:5.0f} Mins".format(finish_cal , total_time ))



print("______________________________________________________________________________________________________________________________________________")
print("\n")
print("\n")
cont = input("                                                                              Press Enter To Continue")

clear()

print("                                      ______                ______            +        ______             ______                                                  ")
print("                                     /     / \   ___      / \     \           +       /     / \         / \     \                                             ")
print("                                     I  50 I ===i    \===== I 50  I           +       I  50 I =========== I 50  I                                                   ")
print("                                     I  LB I ==== iiii===== I LB  I           +       I  LB I =========== I LB  I                                                  ")
print("                                     \ ____\ / /    i     \ /_____/           +       \ ____\ /         \ /_____/                                            ")
print("                                               /    i                         +           gggggggg     oooooooo    oooooooo      dddddddd                            ")
print("                                               /    i   ____  ____            +          ggg   gggg    ooo   ooo   ooo   ooo     ddd   dddd                          ")
print("                                               i     \_/    \/    \___        +          ggg           ooo   ooo   ooo   ooo     ddd    ddd                       ")
print("                                               i         ___ /     \          +          ggg   ggg     ooo   ooo   ooo   ooo     ddd    ddd                        ")
print("                                                \ _   /        ___            +           ggg   gg     ooo   ooo   ooo   ooo     ddd    ddd                      ")
print("                                                  \_______/__/   \            +            ggggggg      ooooooo     ooooooo      ddddddddd                                     ")
print("                                                                              +                                                 ")
print("                                                                              +             llll         uuu    uuu    cccccccc     kkk  kkk               ")
print("                                                                              +             llll         uuu    uuu   ccc     cc    kkk kk           ")
print("                                                                              +             llll         uuu    uuu   ccc           kk kk       ")
print("                                                                              +             llll         uuu    uuu   ccc           kkkk       ")
print("                                                                              +             llllllllll   uuu    uuu   ccc     cc    kk  kkk               ")
print("                                                                              +             llllllllll     uuuuuuu     cccccccc     kkk   kkk                      ")
print("                                                                              +                                                    t")
print("                                                                                                                               t")
print("\n")
print("\n")
print("                                                                       Finish Today's workout        ")
print("\n")
print("                                                                       Today's Workout")

print("\n")
print("\n")
print("                              {0:16}            {1:16}       {2:16}        {3:16}          {4:16}  ".format("Exercise." ,"sets", "Reps", "calories Burned", "time Mins"))   #headers
print("\n")
print("                         {0:16}   {1:16}       {2:16}            {3:16.0f}         {4:16.0f}  ".format(first, sets, reps, first_totalcal, first_time_exercise))  
sleep(0.5)
print("                         {0:16}   {1:16}       {2:16}            {3:16.0f}         {4:16.0f}  ".format(second, sets, reps, second_totalcal, second_time_exercise)) 
sleep(0.5)
print("                         {0:16}   {1:16}       {2:16}            {3:16.0f}         {4:16.0f}  ".format(third, sets, reps, third_totalcal, third_time_exercise )) 

finish_cal = cal_perday * -1
total_time = first_time_exercise + second_time_exercise + third_time_exercise
print("\n")
print("                                                                                           Workout                           Total")
print("                                                                                           Cal Burned:  {0:6.0f} Cal            Time:{1:5.0f} Mins".format(finish_cal , total_time ))

print("\n")
print("\n")
print("\n")
exit = input("                                                          PRESS X TO EXIT")

if exit == "x" or exit == "X":
    clear()
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("                                                                            Thank you")    
    print("\n")
    print("                                                                             Goodbye")

    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

