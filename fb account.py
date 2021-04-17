name=input("enter the name:")
if name>"a"and name<"z":
    surname=input("enter the surname")
    id=input("enter your email address or phone number")
    if id>"a"and id<"z"or id>"0" and id<"9"or id=="@":
        password=input("enter the password")
        if password>"a"and password <"z"or password<"9"or password=="@":
            print("its strong password")
            date=(input("enter the birth of date"))
            if date>"0" and date<"9":
                gender=input("enter the gender")
                if gender=="female"or gender=="male":
                    print("your account is created successfully")
                else:
                    print("abx")
            else:
                print("qwert")  
        else:
            print("yuiop")
    else:
        print("fjjj")  
else:
    print("hhfjc")                            
                        

