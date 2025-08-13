class funmultiple():
    def Subfields():
        print("Sub-fields in AI are:")
        Subfields = "Sub-fields in AI are:"
        print("Machine Learning")
        Subfields ="Machine Learning"
        print("Neural Networks")
        Subfields ="Neural Networks"
        print("Vision")
        Subfields ="Vision"
        print("Robotics")
        Subfields ="Robotics"
        print("Speech Processing")
        Subfields ="Speech Processing" 
        print("Natural Language Processing")
        Subfields ="Natural Language Processing"
       
    def OddEven():
        num = int(input("Enter a number:"))
        if(num % 2 == 0):
            print(num, " is Even Number")
            OddEven = "Even Number"
        else:
            print(num, " is odd Number")
            OddEven = "Odd Number"
            return OddEven 
            
    def Elegible():
        Gender = input("Your Gender:")
        num = int(input("Your Age:"))
        if(Gender == "Female"):
            if(num>=18):
                print("ELIGIBLE")
                marriage="ELIGIBLE"
            else:
                print("NOT ElIGIBLE")
                marriage = "NOT ElIGIBLE"
        if(Gender == "Male"):
            if(num>=21):
                print("ELIGIBLE")
                marriage="ELIGIBLE"
            else:
                print("NOT ElIGIBLE")
                marriage = "NOT ElIGIBLE"
                return marriage
    
    def percentage():
       
       num1 = int(input("Subject1="))
       num2 = int(input("Subject2="))
       num3 = int(input("Subject3="))
       num4 = int(input("Subject4="))
       num5 = int(input("Subject5="))
       Total = num1+num2+num3+num4+num5
       print("Total:",Total)
       Average = Total/5.00
       print("Percentage :",Average)
       return Average

    def triangle():
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        print("Area formula:(Height*Breadth)/2")
        Area_of_Triangle = (Height*Breadth)/2
        print("Area of Triangle:",Area_of_Triangle)
        Height1 = int(input("Height1:"))
        Height2 = int(input("Height2:"))
        Breadth = int(input("Breadth:"))
        print("Perimeter of Triangle:Height1+Height2+Breadth")
        Perimeter_of_Triangle = Height1+Height2+Breadth
        print("Perimeter of Triangle:",Perimeter_of_Triangle)
        return (Area_of_Triangle,Perimeter_of_Triangle)
    
     

