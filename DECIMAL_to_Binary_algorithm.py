#This program will convert all positive integers to binary and,#
#its automation algorithm will put developer defined message on,#
#screen if algorithm is not capable to handle the input.#

#takes user input#
usrint=(input("ENTER NUMBER IN DECIMAL TO BE CONVERTED IN BINARY :: "))
#automation algorithm for input other then expected!#
if usrint.isdigit():
    #conversion of input to int if int#
    usrint=int(usrint)
    de_rslt=""
    de_acc=""
    #function for operations under conversion#
    def to_bin(gt):
        if gt>1:
            global de_rslt
            de_rslt+=str(gt%2)
            to_bin(gt//2)
            #display message if userinput is negative!#
        elif gt<1 & gt!=0:exit("SORRY ALGORITHM NOT FOUND for your INPUT ! :: ("+str(usrint)+") ! dora_err_r:404")
    #calling conversion function!#
    to_bin(usrint)
    #some automation for output#
    if usrint%2==0:de_rslt+="0"
    else:de_rslt+="1"
    i=len(de_rslt)-1
    while i>=0:
        de_acc+=de_rslt[i]
        i=i-1
        #printing output for user!#
    print("Binary of (",usrint,") is :: ","0b"+de_acc)
    #displaying error message for input other then expected!#
else:exit("SORRY ALGORITHM NOT DEFINED FOR STRINGS ! :: ("+str(usrint)+") ! dora_err_r:404")
