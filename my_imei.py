
import re
import math 

print("")
print("imei calculator".upper().center(50))


while True:

    imei_to_list=[]
    all_odds=[]
    all_evens=[]
    doubled_even=[]
    even_total=0
    odd_total=0
    
    imei=input("ENTER IMEI: ")
    if re.search(r"\D",imei)  or imei=="":
        print("please enter 14 digits")
        print("")
    elif len(imei)<14:
        print("invalid length")
        print("imei less than 14 digits")
        print("")
    elif len(imei)>14:
        print("invalid length")
        print("imei greater then 14 digits")
        print("")
    else:
        imei_to_list=list(imei)
        all_odds=imei_to_list[::2]
        all_evens=imei_to_list[1::2]
        
        for x in all_evens:
            h=int(x)*2
            doubled_even.append(str(h))
        doubled_even="".join(doubled_even)
        
        for x in doubled_even:
            even_total+=int(x)
        all_odds="".join(all_odds)
        
        for x in all_odds:
            odd_total+=int(x)
        add_up=even_total+odd_total
        divide_up=add_up%10
        
        if divide_up==0:
            print("")
            print("full imei: ",
            	imei+str(divide_up))
            	
            print("luhn digit: ",
            	math.floor(divide_up))
            print("")
        else:
            after_sub=10-divide_up
            print("")
            print("full imei: ",
            	imei+str(after_sub))
            	
            print("luhn digit: ",
            	math.floor(after_sub))
            print("")
        
        



### vitriol...