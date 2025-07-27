#create a file call it add4.py . 
# now write a python code that will multply three numbers together 6,7, 8 and 
# check if the result is greter than 1000 if yes say hello is greater than 1000 
# if less say oh no  is less than 100
a=6
b=7
c=8
d=(a*b*c)
print(d)
if d>1000:
    print("greater than 1000")
else:
    print("less than 1000")

    #same program using function
    def add():
     a=6
     b=7
     c=8
     d=(a*b*c)
     print(d)
    if d>1000:
     print("greater than 1000")
    else:
     print("less than 1000")
    add()
     