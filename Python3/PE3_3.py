#Calculate the BMI. Save the code as PE3_3.py.
#a) Prompt and request the input for height(cm) and weight(kg) from the console.
#b) Compute the body mass index and print it in three decimal places.
height=float(input("Enter the height in cm:",180))
weight=float(input("Enter the weight18 in kg:",90.5))
BMI=(weight/height**2)*703
print(BMI)