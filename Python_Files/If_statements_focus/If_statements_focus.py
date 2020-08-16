
#Saimer Nieves      Lab 6A



#_______________________________________________________________


#Dictionary


#ip_input--- Ip being inputed by the user
#ip_list    Ip inputed by the user but split into different categories
#ip_type    First Octet of IP list 
#another    Variable assigned to iniciate while loop to add another IP address
#________________________________________________________________


#Loop Entrance
print("\n")
print("                                IP TYPE PROGRAM")            #Title
print("\n")
print("\n")

ip_input = input("What is your IP Adress?  ")               # Ip being inputed by the user
print("\n")
print("             IP ENTERED:  ",ip_input )               #Display output of IP being inserted

    

ip_list = ip_input.split(".")           #new list of Ip inserted through the Split function

print("\n")
ip_type = int(ip_list[0])               #Identification of first variable in IP list



#IP divider

if ip_type >= 1 and ip_type <= 127:             #restrictions for a Class A IP
    print("             Your IP Type is a class A")     #Output display identifying user if IP type

if ip_type >= 128 and ip_type <= 191:           #restrictions for a Class b IP
    print("             Your IP Type is a class B")     #Output display identifying user if IP type

if  ip_type >= 192 and ip_type <= 223:          #restrictions for a Class c IP
    print ("             Your IP type is a class C")        #Output display identifying user if IP type

if ip_type > 223 :                              #restrictions any other IP
    print("              This is NOT an  (  A, B or C  )   IP Address.")        #Output display identifying user if IP type

print("\n")





another = input("Would like to enter another IP?  ")    #Answer to entrence to while loop
print("\n")





#Loop 
while another == "y" or another == "Y":         #Key to entering while loop

    ip_input = input("What is your IP Adress?  ")   # Ip being inputed by the user
    print("\n")
    print("             IP ENTERED:  ",ip_input )#Display output of IP being inserted
    print("\n")
    

    ip_list = ip_input.split(".")
    ip_type = int(ip_list[0])#Identification of first variable in IP list
    
    if ip_type >= 1 and ip_type <= 127:
        print("             Your IP type is a class A")#restrictions for a Class A IP


    elif ip_type >= 128 and ip_type <= 191:
        print("             Your IP Type is a class B")#restrictions for a Class b IP

    elif ip_type >= 192 and ip_type <= 223:
        print ("             Your IP type is a class C")#restrictions for a Class c IP

    else :      #any other IP type
        print("             This is NOT an  (  A, B or C  )   IP Address.")#Output display identifying user if IP type
        


    print("\n")


    another = input("Would you like to enter another IP Address? ")         #Answer to entrence to while loop and repeat the process again
    print("\n")


print("                   Thank You for Using our IP Type program")     #Good bye messages Thanking the user for using our program and informing them they exited loop and program is over
print("\n")
print("                              GOODBYE !")