

COVID TEST:

report=input("do you have covid report")
if report=="yes":
    print("come in navgurukul")
    print("dont go in quartine")
    print("come in room 404")
    bed=input("enter the bed number")
    if bed>"0" and bed<="6":
        print("bed is full")
        bed2=input("enter the bed number")
        if bed2>"6" and bed2<"10":
            print("bed is empty you can stay here" )
        else:
            print("not empty")    
    else:
        print("take other option")        
else:
    print("go to quartine room for 7 days")

