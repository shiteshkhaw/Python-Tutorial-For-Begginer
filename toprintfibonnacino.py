def fibno(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibno(num-2)+fibno(num-1)

num=int(input("Enter A No :"))
for i in range (0,num):
    print(fibno(i), end = ' ')





# def fn(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     return fn(num-2)+fn(num-1)

# num= int(input("enter number :"))
# for i in range (0,num):
#     print(fn(i),end=' ')