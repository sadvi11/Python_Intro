list =[20,50,70,10,90,100,199,159]
print (sum(list))
total=0
for i in list:
    #print(i)
    total=total+i
print(total)
if total>500:
    new = total*20
    print(new)
else:
    new=total/3
    print(new)
    
    

