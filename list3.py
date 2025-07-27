list =[244,399,509,609,709,109,19,90]
total=0
for i in list:
    #print(i)
    total=total+i
print(total)
if total>10029:
    new = total*50
    print(new)
else:
    new=total-600
    print(new)