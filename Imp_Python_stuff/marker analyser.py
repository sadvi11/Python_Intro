#Student Marks Analyzer
#Objective:
#Accept marks from user


#Store in a list


#Display total, average, highest, lowest


#Grade the student based on average




print("🎓 Student Marks Analyzer")
marks = []

# Step 1: Collect marks
num_subjects = int(input("Enter number of subjects: "))

for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# Step 2: Basic analysis
total = sum(marks)
average = total / num_subjects
highest = max(marks)
lowest = min(marks)

# Step 3: Print report
print("\n📊 Report:")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")

# Step 4: Grade assignment
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D or F"

print(f"Grade: {grade}")

