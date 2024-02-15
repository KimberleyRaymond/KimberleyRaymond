 # Variables
# J. Sun

## Demonstrate use of the input()
letGrade = input("Enter your grade(A-F): ")
print("Grade:", letGrade)
#my input is an integer
numGrade = int(input("Enter your grade(0 - 100): "))
print("Grade:", numGrade+40)
#my input is a floating number
average = float(input("Enter your average(0.0 - 100.0): "))
print("Average:", average/2)
#eval produces a numer (integer)
gpa = eval(input("Enter your GPA(0 - 4): "))
print("GPA:", gpa)



'''
## Demonstrate use of the try statement with except clauses
# Python provides a mechanism that called exception handling that allows
# the programmer to report and recover from errors that occur during run time
try:
    letGrade = input("Enter your grade(A-F): ")
    numGrade = int(input("Enter your grade(0 - 100): "))
    #average = float(input("Enter your average(0.0 - 100.0): "))
    #gpa = eval(input("Enter your GPA(0 - 4): "))

    print("Grade:", letGrade)
    print("Grade:", numGrade+100)
    #print("Average:", average/2)
    #print("GPA:", gpa)
    print()

except:
    print("Exceptions: Something went wrong.")
'''
