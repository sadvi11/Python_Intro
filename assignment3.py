#Create a file call it Assignment3.py
#I.  Write a python input that collects three numbers first_number, second_number, third_number 
#Ii. Find the total of all these numbers and display(print) them out
#Iii. Now check if the total is greater than 2000 , print it is greater than 2000
#Immediately multiply your total by 50 and print out the final result
#Iv. Else
        # Print total  is less than 2000
         #immediately multiply your total by 3 and print out the final result


print("enter first number")
firstnumber=(input())
print("enter second number")
secondnumber=(input())
print("enter third number")
thirdnumber=(input())
total=firstnumber+secondnumber+thirdnumber
print(str(total))
if int(total)>200:
    print("yes it is grearter than 200")
    a=total*50
    print("this is the final result",a)
else:
    
    print("no it is less than 200")
    b=total*3
    print("this is the final result",b)

