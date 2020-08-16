

#Saimer Nieves Lab 5 Part A




#Dictionary  
#Beginning_Balance   the inital balance for the account
#Interest_balance    the total amount of accumulated interest
#number_years       total number of years for calculation
#monthly_deposit     amount deposited each month
#interest_rate      the rate for the interest of the account
#year      total number of months for a year
#total_percent      whole percent to conver to decimal
#number_month        number of current month
#total_months         final months total
#monthly_total         amount of beginning balance plus monthly deposit
#interest_percent       converstion of interest into decimal
#interest_balance       amount in dollars of interst
#new_interestbalance      accumulated interest
#low_range      minimal month number to be calculated
#high_range     Maximum month number to be calculated and limit the display
#Proceed        code input of to pr


beginning_balance = 0        #beginning balance
interest_balance = 0         #interest storage balance
beginning_balance = float(input("what is your beginning balance: $"))  #input for beginning balance
print("\n")
number_years = float(input("what is the number of years: "))            #input for number of years
print("\n")
monthly_deposit = float(input("what is your monthly deposit: $"))   #input for monthly deposit
print("\n")
interest_rate = float(input("what is your interest rate: %"))   #input for interest rate
print("\n")
year = 12       #total number of months for a year

total_percent = 100 #whole percent to conver to decimal
number_month = 1 # number of current month
low_range = 0
high_range = 18





total_months = number_years * year                  #formula for total months of years
monthly_total = beginning_balance + monthly_deposit     #total amount of beginning balance plus monthly deposit


interest_percent = (interest_rate / total_percent)/ year # conversion of interest percent into decimal


interest_balance =  (beginning_balance * interest_percent) #amount of interset in dollars






print("      {0:10}    {1:10} \t     {2:10}      {3:10}".format("MONTH" ,"INITIAL", "MONTHLY", "ENDING"))   #headers
print("      {0:10}    {1:10} \t     {2:10}      {3:10}".format("NUMBER" ,"BALANCE.", "INTEREST", "AMOUNT"))


#Beginning of loop 

while number_month <= total_months: #while loop entrance
    ending_balance = beginning_balance + interest_balance + monthly_deposit   #ending balance of sum of all amounts
    print("{0:10.0f}\t {1:10,.2f} \t {2:10,.2f} \t {3:10,.2f}".format(number_month,beginning_balance,  interest_balance, ending_balance)) # output of amounts calculated   


    #EVERYTHIN IS A COPY OF LAB 4 A EXCEPT THIS PART IS NEW----------------------------------------------------------------------------------------------------

#If statement diving number of months by 18 to display 18 months at a time 
    if   number_month == high_range :
         print("\n")
         proceed = input("Press Enter to  view Next 18 Months: ")   #Input statement to continue to the next 18 months by pressing enter
         print("\n")
         print(".")
         print("NEXT 18 MONTHS: ")  #output of next 18 months header
         print("\n")
         high_range = high_range + 18
#=============================================================================================================================================================================
        
    beginning_balance = ending_balance #updating balance

    new_interestbalance = (ending_balance * interest_percent)   #updating new interest balance
    interest_balance = new_interestbalance  #resetting old balance to new balance
    
    
    
    number_month = number_month + 1  #updating months
    


#end of code
   

   

