from os import system
from time import sleep
city_data={"203":"Terminal (203) :: Location : Delhi ISBT"
,"234":"Pune S-4"
,"392":"Jaipur J5"
,"344":"Merut SC-Volvo-4"
,"103":"Mathura Stop 44"
,"156":"Mumbai Bandra stop 33"
,"200":"Dehradun UT4"
,"123":"Aligarh KL87"
,"220":"Nasik Sector-34"
,"345":"Gorakhpur Station 17D"
,"196":"Haydrabad RC-3"
,"202":"Ahemdabad Min-45"
,"123":"Kolkata Jn-45"
,"267":"Chennai jn-78"
,"330":"Agra Ehsaan-56"
,"345":"Surat NTO OFC 56T"
,"349":"Lucknow RT67"
,"299":"Jodhpur Op-78"
,"333":"Amritsar Block 5"
,"334":"Indore NC-44"
,"442":"Chandigarh Bilal-66"
,"256":"Mysuru M-56"
,"293":"Noida Sector 56"
,"344":"Gurugram Sector 56"
,"284":"Shimla BG6 Housing Area-55"}
def service_algo():
    service_algo.u_data=[]
    print(" Here are the cities in which our train service is interlinked.\n\n")
    for a in city_data:
        print(" Terminal ("+str(a)+") :: Location : ",city_data[a])
    print("\n *Enter terminal no. in fields as a city code to book tickets *")
    print("\n You want to travel ,")
def reg():
    reg.to=str(input(" To : "))
    if reg.to in city_data:
        if reg.to in service_algo.u_data:
            print(" ! Hey are you dumb , you have already registered it ! re-enter it ,")
            reg()
        service_algo.u_data.append(reg.to)
        return(0)
    else:
        print(" Oops ! Please enter the corret city\n")
        reg()

def fromd():
    fromd.ul=str(input(" From : "))
    if fromd.ul in city_data:
        service_algo.u_data.append(fromd.ul)
        reg()
    else:
        print(" Oops ! Please enter the corret city\n")
        fromd()
uname=str(input(" Hey welcome to our Travel service for * Business class Travelling *.\n\n Fill your Name : "))
print("\n WELCOME "+uname+", now you can go with your travel planning with optimum rates.\n")
info=str(input("\n "+uname+" what is the reason for your travelling ? , please let us know : "))
print(" Please wait..",end='')
#sleep(2)
print("..")
#sleep(2)
system("clear")
service_algo()
fromd()
exp=10
while(exp<100):
 reg()
 tmp=str(input(" Do not enter Y to travel more : "))
 if tmp=="Y" or tmp=='y':break
total=0
print(" You are travelling from "+city_data[service_algo.u_data[0]],end='')
total+=int(service_algo.u_data[1])
for u in range(1,len(service_algo.u_data)):
    print(" to",city_data[service_algo.u_data[u]],end='')
    total+=int(service_algo.u_data[u])
print("\n Nishant Your Total Bill : "+str(total*5/3)+" INR \n\n")
