# Module-11_Lab-11
# author - cesar
# date - 2025-04-30
"""
Exercises 9.1, 9.2, and 9.3 - Class Averages
"""

def writeGrades():
    # This function writes any number of grades and stores them in a 'grades.txt' file
    with open("grades.txt", "w") as grades:
        count = 0
        while True:
            grade = input("Enter a grade (or 'q' to quit): ")
            if grade.lower() == 'q': 
                break 
            try:
                grade = float(grade) 
                if (0 <= grade) and (grade <= 100): 
                    count += 1 # Increment the count of grades
                    grades.write(f"{grade}\n") # Write the grade to the file
                    print(f"Grade {count} added to the file")
                else:
                    print("Enter a grade between 0 and 100")
            except ValueError:
                print("Invalid input, enter a valid number or 'q' to quit")

def readGrades():
    """
    This function reads the grades from the 'grades.txt' file, 
    counts them, and calculates the average.
    """
    try:
        with open("grades.txt", "r") as grades:
            total = 0
            count = 0
            for line in grades:
                try:
                    grade = int(line.strip())
                    print(f"Grade {count+1}: {grade}")
                    total += grade
                    count += 1
                except ValueError:
                    print(f"Invalid grade")
            if count > 0:
                average = total / count
                print(f"Average grade: {average:.2f}")
            else:
                print("No valid grades found")
    except FileNotFoundError:
        print("file does not exist")

def writeStudentRecord():
    """
    This function writes student records to a csv file
    In the format: "firstName, lastName, exam1grade, exam2grade, exam3grade"
    """
    with open("students.csv", "w") as students:
        while True:
            # Prompt user for first name
            first_name = getValidName("Enter the student's first name (or 'q' to quit): ")
  
            # Prompt user for last name
            last_name = getValidName("Enter the student's last name (or 'q' to quit): ")

            # Prompt user for exam grades
            exam1 = getValidGrade("Enter grade for exam 1 (or 'q' to quit): ")
            exam2 = getValidGrade("Enter grade for exam 2 (or 'q' to quit): ")
            exam3 = getValidGrade("Enter grade for exam 3 (or 'q' to quit): ")
            
            # Dislay the student information
            print(f"Student Name: {first_name} {last_name}, Exam 1: {exam1}, Exam 2: {exam2}, Exam 3: {exam3}")
            
            # Check with user if information is correct before writing to file
            confirm = getValidConfirm("Is this information correct? (y/n): ")

            if confirm == 'y':
                students.write(f"{first_name},{last_name},{exam1},{exam2},{exam3}\n")
                print("Student record added")
            else:
                print("Student record not added")

            continue_entry = getValidConfirm("Do you want to enter another student record? (y/n): ")
            if continue_entry == 'n':
                break

def getValidName(message):
    # This function checks if a name is valid
    name = input(message)
    while True:
        if not name.isalpha():
            print("Invalid name, enter a valid name (letters only)")
            name = input(message)
        else:
            return name

def getValidGrade(message):
    # This function validates grade input
    while True:
        grade = input(message)
        if grade.lower() == 'q':
            return grade
        try:
            grade = int(grade)
            if (grade >= 0) and (grade <= 100):
                return grade
            else:
                print("Invalid grade, enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input, enter a number or 'q' to quit.")

def getValidConfirm(message):
    # This function checks the user confirmation input
    while True:
        confirm = input(message).lower()
        if confirm in ['y', 'n']:
            return confirm
        else:
            print("Invalid input, enter 'y' or 'n'")

def main():
    writeGrades()
    readGrades()
    writeStudentRecord()

main()
