class SampleClass():
#List out the items using function
    def SubFields():
        print("Sub Fields in AI are:")
        lists=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        for item in lists:
            print(item)
           # return lists


#check the given number is odd or even using function
    def OddEven():
        num=int(input("Enter a number"))
        if(num%2==0):
            print(num, "is Even Number")
        else:
            print(num, "is Odd Number")
        #return num


#function to check marriage eligibility
    def Eligible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Gender=='male' and Age>=21):
            print("ELIGIBLE")
            #message="eligible"
        elif(Gender=='female' and Age>=18):
            print("ELIGIBLE")
            #message="eligible"
        else:
            print("NOT ELIGIBLE")
            #message="not eligible"
       # return message


#Percentage Calculation
    def Percentage():
        Sub1=int(input("Subject 1 ="))
        Sub2=int(input("Subject 2 ="))
        Sub3=int(input("Subject 3 ="))
        Sub4=int(input("Subject 4 ="))
        Sub5=int(input("Subject 5 ="))
        Total=Sub1+Sub2+Sub3+Sub4+Sub5
        print("Total :",Total)
        Percentage=(Total/500)*100
        print("Percentage:",Percentage)
        #return Percentage


#print Area and Perimeter of a Triangle
    def Triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth"))
        Area=(Height*Breadth)/2
        print("Area Formula (Height*Breadth)/2")
        print("Area of Triangle :", Area)
        Height1=int(input("Height 1:"))
        Height2=int(input("Height 2:"))
        Breadth=int(input("Breadth"))
        Perimeter=Height1+Height2+Breadth
        print("Perimeter Formula Height1+Height2+Breadth")
        print("Perimeter of Triangle :", Perimeter)
        #return Area,Perimeter