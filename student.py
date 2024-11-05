# Get the number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Initialize a list to store the grades
grades = []

# Collect grades for each subject
for i in range(num_subjects):
    grade = float(input(f"Enter grade for subject {i+1}: "))
    grades.append(grade)

# Calculate the average
average_grade = sum(grades) / num_subjects

# Display the average grade
print(f"The average grade is: {average_grade:.2f}")
