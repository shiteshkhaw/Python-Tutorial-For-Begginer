#Simple Interest Calculator

print("~~~~~~~~~~~~~Calculate Simple Interest~~~~~~~~~~~~~ ")

def inputData():
    name=input("Enter your name : ")
    p=int(input("Enter Principal amount :"))
    n=int(input("Enter No of years :"))
    r=float(input("Enter Rate Of Interest"))
    Calsi(name,p,n,r)

def Calsi(name,p,n,r):
    print("Hello",name)
    SI = (p*n*r)/100
    amt = p + SI
    display(name,p,n,r,SI,amt)

def display(name,p,n,r,SI,amt):
    print("Principal :",p)
    print("No Of Year :",n)
    print("Rate :",r)
    print("Your Simple Interest :",SI)
    print("Total amount is :",amt)

If_name_="_main_"
inputData()
    
