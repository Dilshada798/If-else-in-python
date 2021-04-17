atm=input("insert the card:")
if atm=="debit card" or atm=="credit card": 
    print("please dont remove your card till transaction complete")
    language=input("select your language:")
    if language=="english":
        print("your proceess in work")
        pin=input("enter the pin:")
        if pin=="1234":
            print("your account are in process")
            transaction=input("select the transaction:")
            if transaction=="cash withdrawal":
                print(" in processing")
                type=input("select the amount")
                if type=="saving" or type=="current"or type=="deposit":
                    print("processing")
                    amount=input("enter the amount")
                    if amount>=500 and amount<=10000:
                        print("collect your cash")
                        receipt=input("do you want printed receipt")
                        if receipt =="yes"or receipt=="no":
                            print("transaction has been done successfully")
                        else:
                            print("thnk you visit again") 
                    else:
                        ("amount is not defined") 
                else:
                    ("wrong") 
            else:
                print("wrong amount you have put")   
        else:
            print("not matching")  
    else:
        print("didnt match")   
else:
    print("nothing")                                           

                


   
     
    