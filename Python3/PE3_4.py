#a)  Prompt and request three integer numbers one by one from the console.
first_num=input("Enter the first number :")
second_num=input("Enter the second number :")
third_num=input("Enter the third number :")

#b) Sort these numbers and print them from smallest to largest. we can use the sorted() function
totalnum = first_num, second_num, third_num
print('Before sorting: ', totalnum)
print('After sorting: ', sorted(totalnum))

#Before sorting:  ('7', '8', '1')
#After sorting:  ['1', '7', '8']