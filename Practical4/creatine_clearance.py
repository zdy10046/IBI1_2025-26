# This program first requests the user to enter the required values and then verifies if all the inputs are valid
# (0<Age<100, 20<Weight<80, 0<Creatine Clearance<100) and then calculates the creatine clearance.
# If the gender is female, the result is multiplied by 0.85, otherwise it is not. The formula used is:
# CrCl = ((140 - age) * weight) / (72 * creatine clearance) * 0.85 (if the gender is female)
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