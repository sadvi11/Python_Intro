#code for how many times sheep is present
sheep=[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
sheepcount=0
presentsheep=[]
for i in sheep:
        
        if i ==True: #meaning present
            sheepcount=sheepcount=+1
            presentsheep.append(i)
            
        else:
            continue
print(presentsheep.count(i)) 
    
 # call the function for the final outcome
