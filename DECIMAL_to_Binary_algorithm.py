usrint=(input("ENTER NUMBER IN DECIMAL TO BE CONVERTED IN BINARY :: "))
if usrint.isdigit():
    usrint=int(usrint)
    de_rslt=""
    de_acc=""
    def to_bin(gt):
        if gt>1:
            global de_rslt
            de_rslt+=str(gt%2)
            to_bin(gt//2)
        elif gt<1 & gt!=0:exit("SORRY ALGORITHM NOT FOUND for your INPUT ! :: ("+str(usrint)+") ! dora_err_r:404")
    to_bin(usrint)
    if usrint%2==0:de_rslt+="0"
    else:de_rslt+="1"
    i=len(de_rslt)-1
    while i>=0:
        de_acc+=de_rslt[i]
        i=i-1
    print("Binary of (",usrint,") is :: ","0b"+de_acc)
else:exit("SORRY ALGORITHM NOT DEFINED FOR STRINGS ! :: ("+str(usrint)+") ! dora_err_r:404")
