listfruit=["orange","orange","orange","apple","apple","apple","apple","apple","apple","banana","pineapple","mango","pawpaw","groundnut"]
#print(listfruit)
#write a python code to loop through the list
for i in listfruit:
    #print(i)
    if i =="apple":
        listfruit.remove(i)
    else:
        continue
    print(listfruit)
    


