user_type=raw_input("user type \n1.owner \n2.customer")
restaurants_list={
    "restaurants":{
        "casa asia":{
            "menu":{
                "thai fried rice":int(220),
                "thai fried chicken":int(280),
                "jeera rice":int(160),
            },
            "owner name":"sailen kakati",
            "rating":float(4.9)
        },
        "yo!japi":{
            "menu":{
                "parampora thali":int(450),
                "gahorir mankho":int(250),
                "hahor mankho":int(300),
            },
            "owner name":"mg",
            "rating":float(4.8)
        }
    }
}
if user_type=="1":
    option_choosed=raw_input("you want to update or not?\n press 1 for update \n press 2 for quit")
    print option_choosed
    if option_choosed=="1":
        choosed_restaurant=raw_input("enter the restaurant in which you want to update:")
        if choosed_restaurant in restaurants_list["restaurants"].keys():
            update=raw_input("add a new\n press yes")
            if update=="yes":
                update_item=raw_input("enter the item name:")
                if update_item in restaurants_list["restaurants"][choosed_restaurant]["menu"]:
                    print"item succesfully updated"
    elif  option_choosed=="2":
        print "bye!"
elif user_type=="2":
    print restaurants_list
    order=raw_input("are you want to order \npress yes")
    if order=="yes":
        restaurent_choosed=raw_input("from which restaurent you want to order?")
        if restaurent_choosed not in restaurants_list["restaurants"].keys():
            print "sorry!restaurent not available!"
        elif restaurent_choosed in restaurants_list["restaurants"].keys():
            customer_order_name=raw_input("Enter your food name:")
            if customer_order_name in restaurants_list["restaurants"][restaurent_choosed]["menu"]:
                total=restaurants_list["restaurants"][restaurent_choosed]["menu"][customer_order_name]
                bill=total+(total*0.1)+(total*0.06)+(total*0.15)
                print "order successfully placed"
                print "your order price is",bill
            else:
                print "unavailable item"
    order_type=raw_input("which type of order you want? \n1.home delivery \n2.walk-in")
    if order_type=="1":
        print "you choose home delivery!"
        print "amount to be paid="+str(bill)
    elif order_type=="2":
        print "you choose walk-in delivery!"
        print "amount to be paid="+str(bill)
    rating=raw_input("please rate us\n Press yes")
    if rating=="yes":
        rating=float(raw_input("your rating is:"))
        restaurants_list["restaurants"][restaurent_choosed]['rating']=rating
        print"Thanks for rating us"
else:
    print "Bye"






