age= int(input("enter the age"))
if age>=5 :
    print("able to go school")
    age=int(input("enter the age"))
    if age>=18:
        print("able to cast vote")
        if age>=21:
            print("able to drive car")
            if age>=24:
                print("able to do marriage")
                if age>=25:
                    print("legally drink")
                else:
                    print("not legally drink")    
            else:
                print("not able to do marriage")
        else:
            print("not able to drink")   
    else:
        print("not able to drive")  
else:
    print("not able to cast vote")                   

         

