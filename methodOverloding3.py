num1 = float(input("Enter your 1st number : "))

class cals:
    def add(self,a=None,b=None,c=None):
        sum=0
        if a!=None and b!=None and c!=None:
            sum = a+b+c
            print("Answer is ",sum)

        elif a!=None and b!=None:
            sum=a+b
            print("Answer is ",sum)

        else:
            sum=a
            print("Answer is ",sum)


myObj = cals()
myObj.add(num1)