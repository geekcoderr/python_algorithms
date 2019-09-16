def fac(no:int) -> int:
    factorial=1
    for i in range(1,no+1):
        factorial*=i
    return factorial
usr_int=int(input("Enter number to be checked :: "))
sm=0
for x in range(0,len(str(usr_int))):
    sm+=fac(int(str(usr_int)[x]))
if usr_int==sm:print("Yes ! it's an strong number")
else:print("No ! is't an strong number")
