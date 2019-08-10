from os import system
import time
def rec():
    fac=input("ENTER THE NUMBER OF WHICH YOU WANT FACTORIAL :: ")
    if fac.isdigit():
        fac=int(fac)
        print("Here is your CONCEPT of Calculating ",str(fac)+"!\nDisplaying",end="")
        ans=1
        for j in range(1,8):
            print(end=".")
            time.sleep(1)
        print('\n',end="Extended Function --->> ( ")
        for i in range(0,fac):
            print(str(fac-i)+"*",end="")
            ans*=(fac-i)
        print('0 )')
        print("{[(-- NOTE :: In factorial 0*n == n --)]}")
        print("Your Factorial is Solved and Your answer is :: ",ans)
        system("pause")
        exit(0)
    else:
        print("SORRY! program is not valid for this type of input (type-->",str(fac),") !\n!!",end=" ")
        system("pause")
        system("cls")
        rec()
rec()
