x=int(input("Enter The value for lower range value : "))
y=int(input("Enter The value for upper range value : "))
print("The Prime no in the given range are : ")
for number in range(x,y+1):
    if number>1:
        for i in range(2,number):
            if number%i ==0:
                break
        else:
            print(number)
