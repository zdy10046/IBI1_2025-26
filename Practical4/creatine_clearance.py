a=int(input("Enter age: "))#age
w=int(input("Enter weight: "))#weight
c=int(input("Enter creatine clearance: "))#creatine clearance
g=str(input("Enter gender (Male/Female): "))#gender
if a>0 and a<100:
    if w>20 and w<80:
        if c>0 and c<100:#confirming that all the variables value is within the right interval
            if g=="Female":
                Q=140-a
                W=Q*w
                E=72*c
                CrCl=W*0.85/E
                print("The creatine clearance is: ",CrCl)
            elif g=="Male":
                Q=140-a
                W=Q*w
                E=72*c
                CrCl=W/E
                print("The creatine clearance is: ",CrCl)
            else:
                print("Invalid gender")
        else:
            print("Invalid creatine clearance value. Please enter a value between 0 and 100.")
    else:
        print("Invalid weight value. Please enter a value between 20 and 80.")
else:
    print("Invalid age value. Please enter a value between 0 and 100.")#the calculation won't start if any of the variables value is out of the right interval