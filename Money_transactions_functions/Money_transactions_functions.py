

#FUNCITIONS-----------------------------------------------------------

def goodbye():#<-FUNCTION HEADER

    print("Thank you for using my program. Goodbye")

def cost_input():

    cost_value = float(input("Enter the cost of the item: $"))

    return cost_value

def discount_calc(items, bc):

    if items < 5: #no discount

        discount_percentage = 0

    elif items <= 10: #5-10, 5% discount

        discount_percentage = 0.05

    elif items < 20: #11-19, 10% discount

        discount_percentage = .1

    else:#20+, 20% discount
        
        discount_percentage = .20

    discount_amount = bc * discount_percentage

    return discount_amount


#BASE PROGRAM CODE----------------------------------------------------

answer = "y"

print("Hello and welcome to my Discount Calculator Program!")

while answer == "y":

    cost = cost_input()
    num_items = int(input("Enter quantity purchasing: "))
    tax = float(input("Enter sales tax as a whole number [5% --> 5]: "))
    tax = tax / 100 #decimal version of tax

    base_cost = cost * num_items

    

    #calculate discount amount
    discount_amt = discount_calc(num_items, base_cost)

    discounted_total = base_cost - discount_amt

    tax_amt = discounted_total * tax

    final_total = discounted_total + tax_amt


    print("BASE COST \t DISCOUNT AMT. \t DISCOUNTED COST \t TAX AMT. \t FINAL TOTAL")

    

    print("{0:9.2f} \t {1:13.2f} \t {2:15.2f} \t {3:8.2f} \t {4:11.2f}".format(base_cost, discount_amt, discounted_total, tax_amt, final_total))


    print("BASE COST:   ${:.2f}".format(base_cost))
    print("DISCOUNT:    ${:.2f}".format(discount_amt))
    print("FINAL TOTAL: ${:.2f}".format(final_total))



    #print("BASE COST: $", base_cost)

    answer = input("Would you like to check another item? [y/n]: ")

goodbye()
goodbye()
goodbye()
goodbye()