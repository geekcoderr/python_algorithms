#Take input from user.. >>
tke=(input("Enter the number to check whether it's an Armstrong number or not :: "))
sumof=0
temp=tke
leng=len(tke)
tke=list(tke)
#Loop will start to compute power of number with length.. >>
for i in range(0,leng):
    tke[i]=int(tke[i])
    sumof+=tke[i]**leng
#Print answer to user if number is armstrong or not.. >>
if sumof==int(temp):
    print("YES ! (",temp,") is an Armstrong Number !")
else:
    print("NO ! (",temp,") is not an Armstrong Number !")
exit(0)
